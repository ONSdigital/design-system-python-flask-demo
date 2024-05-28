# design-system-python-flask-demo

This project is demo of design system implemented in Python and Flask.

## Requirements setup

For setting up this project, run the below command. pyenv is a python version management tool that allows switching between
multiple python versions. jq is a JSON preprocessor that is used to fetch the design systems templates using the `scripts/load_release.sh`.

```
brew install pyenv jq
```

To install the python and initialize virtual env run the following commands. Note:- The python version is specified in the
`.python-version` file.

```
pyenv install
```

```
python3 -m venv env && source env/bin/activate
```

For installing flask run.
We are also using installing YAML frontmatter in this step to facilitate DS examples that use settings like `"fullWidth": true`

```
pip install Flask python-frontmatter
```

## Running the Application

For running this application, run `make run` which first executes `scripts/load_release.sh` script that downloads the Design System macros zip file from the github release and unzips them into a templates folder. Then, `flask --app application run ` renders all the example components as displayed in the Design System at `http://127.0.0.1:5000`. The CSS and JS are pulled in at runtime from the CDN.
