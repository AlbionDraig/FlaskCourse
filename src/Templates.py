# RUN APP
# flask --app .\src\Templates.py run
# flask --app .\src\Templates.py --debug run

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__, template_folder='../templates')

@app.add_template_filter
# app.add_template_filter(format_date, name='format_date')
def format_date(date, format='%Y-%m-%d'):
    return date.strftime(format)

@app.route('/')
def index():
    page_name = 'Home'
    datetime_now = datetime.now()
    return render_template(
        'home.html', 
        datetime_now=datetime_now,
        page_name=page_name
    )

@app.route('/<string:name>')
def greeting(name=None):
    data = ['Hello', 'World', 'Flask', 'Python']
    return render_template('demo.html', name=name, data=data)