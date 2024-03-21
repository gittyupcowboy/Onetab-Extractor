from bs4 import BeautifulSoup
import re

# Function to directly return the creation date string
def format_creation_date(date_str):
    return date_str.strip()

# Initialize variables for holding group data and continuous link numbering
tab_groups = []
link_number = 1
total_links_count = 0

# Path to your HTML file
input_file_path = 'OneTab.htm'
output_file_path = 'ExtractedLinksFormatted.md'

# Reading the HTML content from the file
with open(input_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find all creation date instances and their corresponding tabs
creation_dates = soup.find_all(text=re.compile('Created \d+/\d+/\d+, \d+:\d+:\d+ [AP]M'))

for date in creation_dates:
    # Extract the text immediately following the creation date, which should be the date itself
    formatted_date = format_creation_date(date)

    # Find the next sibling which contains the links for this date's group
    tab_list = date.parent.parent.parent.find_next(class_="tabList")
    if not tab_list:
        continue

    links = tab_list.select('.tabLink')
    markdown_links = []
    for link in links:
        markdown_links.append(f"{link_number}. [{link.get_text()}]({link['href']})  ")
        link_number += 1
        total_links_count += 1

    # Add formatted date as a Markdown header
    tab_groups.append({
        'creation_date': f"### {formatted_date}\n",
        'links': markdown_links
    })

# Write the extracted information to a file, formatting links as list items under each date group
with open(output_file_path, 'w', encoding='utf-8') as file:
    for group in tab_groups:
        # Write the creation date as a header
        file.write(group['creation_date'] + "  \n")
        for link in group['links']:
            file.write(link + "\n")
        file.write("\n")  # Extra newline for spacing between groups

print(f"Formatted links have been saved to {output_file_path}")
print(f"Total links extracted: {total_links_count}")
