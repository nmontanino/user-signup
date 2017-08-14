from flask import Flask, request, redirect, render_template
# import cgi
# import os
# import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

# template_dir = os.path.join(os.path.dirname(__file__), 'templates')
# jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

@app.route("/")
def index():
    return render_template('index.html')

app.run()

