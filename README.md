# OneTab Extractor Script v1.0
`onetab_extractor.py`, is designed to parse/extract links from OneTab.htm, organize said links into groups by their creation date, and save as a markdown file. Each link is numbered sequentially across all tab groups, with each group preceded by its creation date.

## How to Use

1. utilize your browsers 'save as' feature on your OneTab page to save to the same directory as the script.  
2. Run the script via:  
   ```
   python onetab_extractor.py
   ```
3. Check the generated `ExtractedLinksFormatted.md` for your formatted links.

## Features

- Extracts links from OneTab's export HTML.
- Formats links in Markdown, with sequential numbering.
- Groups links by their creation date for better organization.

---

## Managing Old Tabs in OneTab

To clear old tabs from OneTab (excluding locked tabs), you can use the JavaScript console in your browser. This can help manage clutter without losing the most recent tabs. Here's how:

### Clearing Old Tabs (Excluding Locked Tabs)

1. Click on the OneTab tab in your browser.
2. Open the JavaScript console. For Firefox:
   - Right-click on the page and choose "Inspect".
   - Click on "Console".
   - Click on the little window that starts with `>>` (not the filter line).
3. Copy and paste the following code as a single operation:

```javascript
window.confirm = function() { return true; };
var keep = 20; // Adjust this to the number of tab groups you wish to keep - be sure to account for locked groups they count against most recent! 
for (x of document.getElementsByClassName("clickable")) {
  if (x && (x.innerHTML == "Delete all") && ((keep--) <= 0)) {
    x.click();
  }
}
```

In case browser console dislikes multi-line entry:  

``` window.confirm = function() { return true; }; var keep = 20; for (x of document.getElementsByClassName("clickable")) { if (x && (x.innerHTML == "Delete all") && ((keep--)<=0)) { x.click(); } } ```


--- 

Adapted from a solution by [u/MultiplyAccumulate](https://old.reddit.com/user/MultiplyAccumulate) on [Reddit](https://old.reddit.com/r/chrome/comments/7svirq/does_anyone_know_how_to_delete_all_onetab/hyhlo3i/) (2022-02-26).

### Additional Information





--- 

