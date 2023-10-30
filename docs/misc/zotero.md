# Zotero Config

Should rename and index .pdf files into the right spot in dropbox.

Install addons: Zotfile, Better BibTeX

Open "Zotfile Preferences":

* general settings > custom location: /Users/max.harper/Dropbox/max/research-papers/zotero
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
    sudo ln -s ./max.harper fmh
    sudo ln -s ./max.harper maxharp3r
    ```
