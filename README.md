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

## Visual Tests

For the visual regression tests BackstopJS is used. To install BackstopJS run:

```
npm install -g backstopjs
```

Note-: Make sure to install npm package([link](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)) before before installing BackstopJS.

To utilize BackstopJS, the workflow is as follows:

`make generate-backstopjs`: This python file generates `backstop.json` file which has the config for BackstopJS

`make test`: This runs the tests which creates a set of screenshots, compares them with reference screenshots and shows any changes in the visual report (`backstop_data/html_report`). Note-: Make sure to keep the local server running before executing this step.

`make approve`: This approves the changes and updates the reference files with the results from `backstop test`.
