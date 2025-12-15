import os

import frontmatter
from flask import (
    Flask,
    abort,
    render_template,
    render_template_string,
    send_from_directory,
)
from jinja2 import ChainableUndefined

app = Flask(__name__)
root_directory = os.path.abspath("templates/components")


def setAttributes(dictionary, attributes):
    for key in attributes:
        dictionary[key] = attributes[key]
    return dictionary


def resolvePath(path):
    """
    Resolve a path inside `templates/components` safely.

    - Prevents path traversal by ensuring the resolved path is under `root_directory`.
    - Returns a filesystem path if it exists; otherwise triggers a 404.
    """

    resolved = os.path.normpath(os.path.join(root_directory, path))

    # Ensure the path is inside the allowed root (prevents ../ traversal)
    if not resolved.startswith(root_directory + os.sep) and resolved != root_directory:
        abort(404)

    # If the path doesn't exist, return 404
    if not os.path.exists(resolved):
        abort(404)

    return resolved


app.jinja_env.filters["setAttributes"] = setAttributes
app.jinja_env.undefined = ChainableUndefined


@app.route("/<path:filename>")
def generate_images(filename):
    return send_from_directory("static/", filename)


@app.route("/")
def index():
    directories = {
        directory
        for directory in os.listdir(root_directory)
        for file in os.listdir(os.path.join(root_directory, directory))
        if file.startswith("example")
    }
    return render_template("index.html", example_files=sorted(directories))


@app.route("/components/<component_name>")
def component(component_name):

    dir = resolvePath(component_name)

    example_files = [file for file in os.listdir(dir) if file.startswith("example")]

    return render_template(
        "component-examples-list.html",
        example_files=sorted(example_files),
        component_name=component_name,
    )


@app.route("/components/<component_name>/<filename>")
def example(component_name, filename):

    file = resolvePath(os.path.join(component_name, filename))

    with open(file, "r") as content:
        content = frontmatter.load(content)
    if "layout" in content.metadata:
        template = content.content
    else:
        template = (
            "{% extends 'layout/_template.njk' %}"
            + "{% block body %}<div class='ons-u-p-m'>"
            + content.content
            + "</div>{% endblock %}"
        )
    return render_template_string(template)


if __name__ == "__main__":
    app.run()
