from flask import Flask, render_template, render_template_string, send_from_directory
from jinja2 import ChainableUndefined
import os, frontmatter

app = Flask(__name__)

def setAttributes(dictionary, attributes):
    for key in attributes:
        dictionary[key] = attributes[key]
    return dictionary

app.jinja_env.filters['setAttributes'] = setAttributes
app.jinja_env.undefined = ChainableUndefined

@app.route('/<path:filename>')
def generate_images(filename):
    return send_from_directory('static/',filename)

@app.route('/')
def index():
    root_directory = 'templates/components'
    directories = {directory for directory in os.listdir(root_directory) for file in os.listdir(os.path.join(root_directory, directory)) if file.startswith('example') }
    return render_template('index.html', example_files=sorted(directories))


@app.route('/components/<component_name>')
def component(component_name):
    example_files = [file for file in os.listdir(f'templates/components/{component_name}/') if file.startswith('example')]
    return render_template('component.html', example_files= sorted(example_files), component_name = component_name)

@app.route('/components/<component_name>/<filename>')
def example(component_name, filename):
    try:
        with open(f'templates/components/{component_name}/{filename}','r') as content:
          content = frontmatter.load(content)
        if 'layout' in content.metadata:
             template =  content.content
        else:
             template = '{% extends "layout/_template.njk" %}{% block body %}<div class="ons-u-p-m">' + content.content + '</div>{% endblock %}'
        return render_template_string(template)
    except FileNotFoundError:
        return "File not found"

if __name__ == "__main__":
    app.run(debug=True)