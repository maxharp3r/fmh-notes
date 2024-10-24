# Macbook setup and notes

## Initial Setup

keyboard/touchpad

* terminal
    * turn on key repeat: `defaults write NSGlobalDomain ApplePressAndHoldEnabled -bool false`
* settings > keyboard
    * change delay and repeat
    * turn off emoji shortcut key: set "Press 🌐 key" to "Do Nothing"
* settings > trackpad
    * tracking speed: (faster)
    * click: light
    * tap to click: on

core apps

* install oh my zsh
* install brew
* install apps:

```sh
# standard
brew install keepingyouawake iterm2 stats rectangle glances
brew install --cask macvim

# dev
brew install glances tlrc

# maybe
brew install dropbox google-chrome
```

* install python: `brew install python3 python@3.9 python@3.10 python@3.11 python@3.12`
* install vscode
    * install via website
    * see `/docs/dev/vs-code.md` for extensions
* git clone this repository
    *
* (old apps -- no longer used)
    * balance-lock
    * sizeup

configure git

```sh
git config --global user.name "(name)"
git config --global user.email (email)
cat ~/.gitconfig
```

note: getting completions to work in oh my zsh: <https://docs.brew.sh/Shell-Completion#configuring-completions-in-zsh>

## Next Steps Setup

* `gmail.md` (only if new google account)
* `chrome.md`

## Google Meet as standalone app

<https://support.google.com/meet/answer/10708569?hl=en>
