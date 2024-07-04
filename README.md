# design-system-python-flask-demo

This project is demo of design system implemented in Python and Flask.

## Setup

For setting up this project, run the below command. pyenv is a Python version management tool that allows switching between multiple Python versions. jq is a JSON preprocessor that is used to fetch the design system's templates using `scripts/load_release.sh`.

```
brew install pyenv jq
```


Install Python and initialize the virtual environment as shown below.
Note: The Python version is specified in the .python-version file.

```
pyenv install
python3 -m venv env && source env/bin/activate
```

Install Poetry, a dependency management and packaging tool, as shown below.

```
pip install -U pip setuptools
pip install poetry
```

All the libraries declared are available in `pyproject.toml`. To install these defined dependencies, run `poetry install`. To add a new dependency, run `poetry add <dependency_name>`.

## Running the Application

For running this application, run `make run` which first executes `scripts/load_release.sh` script that downloads the Design System macros zip file from the github release and unzips them into a templates folder. Then, `flask --app application run ` renders all the example components as displayed in the Design System at `http://127.0.0.1:5000`. The CSS and JS are pulled in at runtime from the CDN.

## Visual Tests

For the visual regression tests BackstopJS is used. To install BackstopJS run:

```
yarn install
```

Note-: Make sure to install yarn package([link](https://classic.yarnpkg.com/lang/en/docs/install/#mac-stable)) before before installing BackstopJS.
