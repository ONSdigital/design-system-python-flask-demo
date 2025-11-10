# design-system-python-flask-demo

This project is a demo of design system implemented in Python and Flask.

## Setup

For setting up this project, run the below command. pyenv is a Python version management tool that allows switching between multiple Python versions. jq is a JSON preprocessor that is used to fetch the design system's templates using `scripts/load_release.sh`.

```
brew install pyenv jq
```

Install Python and initialise the virtual environment.
Note: The Python version is specified in the .python-version file.

```
pyenv install
```

- ignore warnings about `tkinter`
- configure your shell <https://github.com/pyenv/pyenv?tab=readme-ov-file#b-set-up-your-shell-environment-for-pyenv>

Install Poetry, a dependency management and packaging tool, as shown below.

```
pip install -U pip setuptools
pip install poetry
```

All the libraries declared are available in `pyproject.toml`. Install these defined dependencies.

```
poetry self add poetry-plugin-dotenv
poetry install
```

To add new dependencies in this project, run `poetry add <dependency_name>`.

Install pre-commit hooks, to automatically execute code checks and formatting tools before each commit.

```
poetry run pre-commit install
```

Install code formatter prettier and `prettier-plugin-jinja-template` plugin.

```
npm install
```

## Running the Application

For running this application, run `make run` which first executes `scripts/load_release.sh` script that downloads the Design System macros zip file from the github release and unzips them into a templates folder. Then, `poetry run flask run` renders all the example components as displayed in the Design System at `http://127.0.0.1:5000`. The CSS and JS are pulled in at runtime from the CDN.

## Updating to the latest version of the Design System

- Simply update the version in the `.design-system-version` file.
- Run the application locally. The latest Design System templates should be downloaded from GitHub in the run script.
- Manually smoke test the application locally, paying attention to any recent changes in the Design System templates.
