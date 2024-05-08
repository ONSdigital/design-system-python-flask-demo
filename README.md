# design-system-python-flask-demo

This project is demo of design system implemenented in Python and Flask.

### Requirements setup

For setting up this project, run the below command. pyenv is a python version management tool that allows switch between
multiple python version. jq is a JSON preprosser that is used to fetch the design systems templates using the `scripts/load_release.sh`.

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

For installing flask run. We are also using installing YAML frontmatter in this step to facilitate DS examples that use settings like `"fullWidth": true`

```
pip install Flask python-frontmatter
```

### Running the Application

For running this application, load and update the design system templates first using the below command.(Make sure to
specify the latest version of design system in `.design-system-version`.)

```
make load-design-system-templates
```

`make load-design-system-templates` loads the `scripts/load_release.sh` that gets all the components and layouts of [design system](https://github.com/ONSdigital/design-system) in a zip file which is created in each [design system release](https://github.com/ONSdigital/design-system/releases) and unloads them to the templates folder. These macros are gitignored.(This is same as [eq_questionnarie_runner](https://github.com/ONSdigital/eq-questionnaire-runner/blob/main/scripts/load_release.sh))

Then, run `make run` which renders all the example components as displayed in the Design System at `http://127.0.0.1:5000`. The CSS and JS are pulled in at runtime from the CDN.

### Visual Tests

To run/automate the Visual Tests, BackstopJs is used, comparing screenshots overtime.To install BackstopJs run

```
npm install -g backstopjs
```

Note-: Make sure to install npm package([link](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)) before before installing BackstopJS.

To utilize BackstopJS, the workflow is as follows:

`make generate-backstopjs`: This python file generates `backstop.json` file with specified Design System URLs,screen sizes, DOM selectors etc.

`backstop test`: This creates a set of screenshots and compares them with reference screenshots and shows any changes in the visual report.(`backstop_data/html_report`).Note-: Make sure to keep the local server running before executing this step.

`backstop approve`: This approves the changes and updates the reference files with the results from `backstop test`.
