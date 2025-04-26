# RUN APP
# flask --app .\src\Templates.py run
# flask --app .\src\Templates.py --debug run

from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates')

@app.route('/')
@app.route('/<string:name>')
def index(name=None):
    data = ['Hello', 'World', 'Flask', 'Python']
    return render_template('demo.html', name=name, data=data)