# design-system-python-flask-demo

This project is a demo site repo for design system using Python and Flask.

## Requirements setup

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

For Installing Flask run

```
pip install Flask
```

### Running the Application

For running this application, load and update the design system templates first using the below command.(Make sure to
specify the latest of design system in `.design-system-version`.)

```
make load-design-system-templates
```

Then, run `make run` which returns a Hello World Page with the basic DS page layout(see `index.html`) at `http://127.0.0.1:5000` .
