Adapted from a solution by [u/MultiplyAccumulate](https://old.reddit.com/user/MultiplyAccumulate) on 

[Reddit](https://old.reddit.com/r/chrome/comments/7svirq/does_anyone_know_how_to_delete_all_onetab/hyhlo3i/) (2022-02-26).


full comment:  

* click on the onetab tab
* Open the javascript console.  On firefox:
   * Right click on the page, choose Inspect
   * click on console
   * click on the little window that starts with >> (not the filter line)
* Copy and paste the code below, as a single paste operation:

Code:

    function delete_single() {
       for (clickable of clickables) {
         if (!clickable || clickable.innerHTML !== "Delete all")
           continue;
         clickable.click();
         return true;
       }
       return false;
     }
     window.confirm = function() { return true; }
     var clickables = document.getElementsByClassName("clickable");
     document.addEventListener('DOMNodeRemoved', delete_single, false);
     delete_single();

This code was archived from the following site that is no longer on the net and is not on the internet archive.

https://j3soon.com/notes/2019/05/29/onetab-delete-all-saved-tabs-script.html

Here is a simpler version that hasn't been extensively tested:

    window.confirm = function() { return true; }; for (x of document.getElementsByClassName("clickable")) { if (x && x.innerHTML == "Delete all") { x.click(); } }

And another version, which leaves two sets of tabs undeleted:

    window.confirm = function() { return true; }; var keep = 2; for (x of document.getElementsByClassName("clickable")) { if (x && (x.innerHTML == "Delete all") && ((keep--)<=0)) { x.click(); } }

That way, you can get rid of the old dreck which is slowing your browser down while still keeping the most recent stuff.