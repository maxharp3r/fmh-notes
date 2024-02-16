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

### notes about pyenv-virtualenv

There is extra work getting pyenv-virtualenv to run (a) in zsh, and (b) in vs-code.

In vscode, add this to `settings.json`:

```json
"python.terminal.activateEnvironment": false
```

edit `.zsh` or `~/.oh-my-zsh/custom/pyenv.zsh`:

```sh
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

plugin=(
  pyenv
)

eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

To verify that pyenv-virtualenv works:

* activate a virtual environment, e.g., `pyenv activate 3.11.6/envs/fmh-sandbox-data`
* verify that `pip --version` shows the path to the environment (not the base environment)
* may have to restart vscode for settings to apply correctly

## using pyenv

```bash
pyenv versions

pyenv which python
pyenv shell 3.11

pyenv install 3.11
```

## using pip

```sh
pip install -r requirements.txt

pip install --upgrade --force-reinstall -r requirements.txt
```

### Specifying versions (pip)

details:

* <https://pip.pypa.io/en/stable/reference/requirement-specifiers/>
* <https://packaging.python.org/en/latest/specifications/version-specifiers/#id4>

```txt
SomeProject
SomeProject == 1.3
SomeProject >= 1.2, < 2.0
SomeProject[foo, bar]
```

## using conda

```sh
conda env list

conda activate ENV_NAME
conda deactivate

conda env create -f env.yml
conda env update -f env.yml --prune
conda remove --name ENV_NAME --all
```

### Specifying versions (conda)

full spec: <https://docs.conda.io/projects/conda-build/en/stable/resources/package-spec.html#package-match-specifications>

```txt
Constraint type            Specification           Result
Fuzzy                      numpy=1.11              1.11.0, 1.11.1, 1.11.2, 1.11.18 etc.
Exact                      numpy==1.11             1.11.0
Greater than or equal to   "numpy>=1.11"           1.11.0 or higher
OR                         "numpy=1.11.1|1.11.3"   1.11.1, 1.11.3
AND                        "numpy>=1.8,<2"         1.8, 1.9, not 2.0
```

### create empty conda env

`conda create --name py38 python=3.8`

### conda is slow

Try the libmamba solver (via <https://stackoverflow.com/a/77090748/293087>):

```sh
conda update -n base conda
conda install -n base conda-libmamba-solver
conda config --set solver libmamba
```

## using poetry

```bash
poetry install

poetry shell
deactivate

# list environments in this project
poetry env list
```

### installing with a specific version of python

<https://python-poetry.org/docs/managing-environments/>

`poetry env use /anaconda/envs/py38/bin/python`

### Specifying versions (poetry)

full spec: <https://python-poetry.org/docs/dependency-specification/>

* `^1.2.3` => `>=1.2.3 <2.0.0`
* `~1.2.3` => `>=1.2.3 <1.3.0`
* `1.2.*`  => `>=1.2.0 <1.3.0`

## creating a virtualenv manually

```bash
python3 -m venv ./env
source ./env/bin/activate
deactivate

# if you need the jupyter kernel, activate the env, then:
source ./env/bin/activate
pip install jupyter
ipython kernel install --name "local-venv" --user

## list jupyter kernels
jupyter kernelspec list
```

## install requirements.txt

```bash
pip install -r requirements.txt

# upgrade
pip install --upgrade --force-reinstall -r requirements.txt
# or
pip install --ignore-installed -r requirements.txt
```

## finding package dependencies

What packages does a pypi package depend on?

Click on the libraries.io link, e.g.: <https://libraries.io/pypi/>

Or, use `pipdeptree` -- <https://stackoverflow.com/a/45561645/293087>

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
