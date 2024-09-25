# Visual Studio Code

## settings

* format on save: on

## extensions

* python
* jupyter
* black formatter
* isort
* makefile tools
* markdownlint
* gitlens
* vscode-pdf

## workspace settings

open control palette: `Preferences: Open Workspace Settings (JSON)`

```json
{
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": "always"
        },
    },
    "markdownlint.config": {
        "MD007": {
            "indent": 4
        }
    }
}
```

## zen mode

To run without fullscreen:

`"zenMode.fullScreen": false`
