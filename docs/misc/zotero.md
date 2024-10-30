# Zotero Config

## Zotero 7+

Install zotero (via brew) and the browser plugin.

Settings to get dropbox syncing working:

* settings > general
    * light
    * "customize filename format":
      `{{ authors max="1" case="lower" suffix="_" }}{{ year suffix="_" }}{{ title case="lower" replaceFrom="\s" replaceTo="_" regexOpts="g" truncate="30" }}`
* settings > sync
    * sign in
    * uncheck the settings related to syncing attachments (we'll use dropbox)
    * close settings and click arrows icon in top right to sync library
* settings > advanced
    * linked attachment base directory:
      `/Users/maxharper/Dropbox/max/research-papers/zotero`
* menu > view > columns
    * add "date modified"
* Install [zotmoov](https://github.com/wileyyugioh/zotmoov) plugin.
* settings > zotmoov
    * "directory to move files to"
      `/Users/maxharper/Dropbox/max/research-papers/zotero`

## Old Zotero 5 instructions

Should rename and index .pdf files into the right spot in dropbox.

Install addons: Zotfile, Better BibTeX

Open "Zotfile Preferences":

* general settings > custom location: /Users/maxharper/Dropbox/max/research-papers/zotero
* renaming rules
    * format string (both fields): {%a_}{%y_}{%t}
    * check: change to lower case, replace blanks, truncate title, max length 30, max authors 1

Open "preferences"

* Sync > sign in to Zotero
* Sync > turn off both "Sync attachment files"

Click the green "sync arrow" button in top right to get metadata

To get older files to open, perhaps create symlinks, e.g.:

    ```sh
    cd ~/..
    sudo ln -s ./maxharper fmh
    sudo ln -s ./maxharper maxharp3r
    sudo ln -s ./maxharper max.harper
    ```
