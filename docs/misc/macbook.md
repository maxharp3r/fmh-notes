# Macbook setup and notes

## Initial Setup

keyboard/touchpad

* terminal
    * turn on key repeat: `defaults write NSGlobalDomain ApplePressAndHoldEnabled -bool false`
* settings > keyboard
    * change delay and repeat
    * turn off emoji shortcut key: set "Press 🌐 key" to "Do Nothing"
    * keyboard shortcuts > function keys > use F1, F2, etc. keys as standard function keys: on
* settings > trackpad
    * tracking speed: (faster)
    * click: light
    * tap to click: on

finder

* finder > settings
    * general: new finder windows show downloads
    * sidebar: uncheck recents, airdrop
* to ensure a directory always opens in list view
    * navigate to folder (start with hard drive root to affect sub-dirs)
    * cmd+j
    * check "always open in list view"
* close settings and drag to reorder left panel

core apps

* install oh my zsh
* install brew
* install apps:

```sh
# standard
brew install keepingyouawake iterm2 stats rectangle google-chrome
brew install --cask macvim

# maybe
brew install dropbox
```

## Dev Setup

```sh
brew install python3 python@3.9 python@3.10 python@3.11 python@3.12
brew install glances tlrc
```

* install vscode
    * install via website
    * see `/docs/dev/vs-code.md` for extensions
* configure git

```sh
git config --global user.name "(name)"
git config --global user.email (email)
cat ~/.gitconfig
```

* configure github with ssh keys
* git clone this repository into `~/code`

## Next Steps Setup

* `gmail.md` (only if new google account)
* `chrome.md`
* additional apps:
    * spotify
    * zoom
    * google meet -- <https://meet.google.com> at the top right of your browser, in the URL bar, click Install
* printer
    * (just add the printer when it's online, don't install 3p software)

## Old Apps

No longer used.

* balance-lock
* sizeup
