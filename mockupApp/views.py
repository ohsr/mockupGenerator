from flask import Flask, render_template, request, abort, url_for
from jinja2 import Environment, FileSystemLoader

import imgkit

app = Flask(__name__)
app.config.from_object("config")


def createMockup(path, variables):
    templateLoader = FileSystemLoader(searchpath="./")
    templateEnv = Environment(loader=templateLoader)
    TEMPLATE_FILE = path
    template = templateEnv.get_template(TEMPLATE_FILE)
    css_url = url_for('static', filename='css/bootstrap.min.css')
    outputText = template.render(var="test", cssurl=css_url, type=variables[0])
    return outputText

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/mockup', methods=['POST'])
def create_mockup():
    content = request.get_json(silent=True)
    if content and "data" in content:
        type = "ecommerce"
        variables = [type]
        imgkit.from_string(createMockup("mockupApp/templates/mockups/apple.html", variables), 'pictures/apple.jpg')
        imgkit.from_string(createMockup("mockupApp/templates/mockups/android.html", variables), 'pictures/android.jpg')
        imgkit.from_string(createMockup("mockupApp/templates/mockups/laptop.html", variables), 'pictures/laptop.jpg')
        imgkit.from_string(createMockup("mockupApp/templates/mockups/tablet.html", variables), 'pictures/tablet.jpg')
        return "OK"
    else:
        abort(422, "Veuillez spécifier des paramètres valables pour générer un Mockup")


@app.route('/cv', methods=['POST'])
def create_cv():
    print("Je passe cv")


if __name__ == "__main__":
    app.run()
