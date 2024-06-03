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

### Running the Application

For running this application, load and update the design system templates first using the below command.(Make sure to
specify the latest version of design system in `.design-system-version`.)

```
make load-design-system-templates
```

`make load-desing-system-templates` loads the `scripts/load_release.sh` that gets all the components and layouts of [design system](https://github.com/ONSdigital/design-system) in a zip file which is created in each [design system release](https://github.com/ONSdigital/design-system/releases) and unloads them to the templates folder. These macros are gitignored.

Then, run `make run` which renders a Hello World Page with the basic DS page layout(see `index.html` which imports the template `layout/_template.njk` ) at `http://127.0.0.1:5000`. The CSS and JS are pulled in at runtime from the CDN.
