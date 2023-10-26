# python

## installing pyenv + conda

The most flexible python setup is to have both `pyenv` and `conda` installed.

* don't use pyenv to install/manage conda, install them separately (using brew)
* a new login shell:
    * should not have any environment activated
    * should have both the `pyenv` and `conda` commands available
    * should use the pyenv default python (no virtualenv) by default

`brew install miniconda pyenv pyenv-virtualenv xz readline`

Follow instructions to configure them for the current shell.

If using oh-my-zsh, move conda config from `~/.zshrc` to a new file `~.oh-my-zsh/custom/conda.zsh`

refs:

* <https://stackoverflow.com/a/58045893/293087>

## using pyenv

```bash
pyenv versions

pyenv which python
pyenv shell 3.11

pyenv install 3.11
```

## using conda

```sh
conda env list
conda activate my-env
conda deactivate
```

## using poetry

```bash
poetry install

poetry shell
deactivate
```

### Specifying versions

full spec: <https://python-poetry.org/docs/dependency-specification/>

* `^1.2.3` => `>=1.2.3 <2.0.0`
* `~1.2.3` => `>=1.2.3 <1.3.0`
* `1.2.*`  => `>=1.2.0 <1.3.0`

## installing python + tkinter via pyenv

Recbole requires tkinter

```bash
brew install tcl-tk
brew --prefix tcl-tk
```

then:

```bash
pyenv uninstall 3.11.1
env \
  PATH="$(brew --prefix tcl-tk)/bin:$PATH" \
  LDFLAGS="-L$(brew --prefix tcl-tk)/lib" \
  CPPFLAGS="-I$(brew --prefix tcl-tk)/include" \
  PKG_CONFIG_PATH="$(brew --prefix tcl-tk)/lib/pkgconfig" \
  CFLAGS="-I$(brew --prefix tcl-tk)/include" \
  PYTHON_CONFIGURE_OPTS="--with-tcltk-includes='-I$(brew --prefix tcl-tk)/include' --with-tcltk-libs='-L$(brew --prefix tcl-tk)/lib -ltcl8.6 -ltk8.6'" \
  pyenv install 3.11.1
```

refs:

* <https://stackoverflow.com/a/60469203/293087>
