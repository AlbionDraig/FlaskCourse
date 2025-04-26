# RUN APP
# flask --app .\src\Templates.py run
# flask --app .\src\Templates.py --debug run

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__, template_folder='../templates')

@app.add_template_filter
def format_date(date, format='%Y-%m-%d'):
    return date.strftime(format)
# app.add_template_filter(format_date, name='format_date')

@app.route('/')
def home():
    page_name = 'Home'
    datetime_now = datetime.now()
    return render_template(
        'home.html', 
        page_name=page_name,
        datetime_now=datetime_now
    )

# Personalized function
@app.add_template_global
def repeat_times(text, times):
    return text * times
# @app.add_template_global(repeat_times, name='repeat_times')

@app.route('/repeat')
@app.route('/repeat/<string:text>/<int:times>')
def repeat(text = '' , times = 0):
    page_name = 'Repeat'
    datetime_now = datetime.now()
    return render_template(
        'repeat.html', 
        page_name=page_name,
        datetime_now=datetime_now,
        text=text,
        times=times,
        # share functions with templates
        # repeat_times=repeat_times
    )

@app.route('/<string:name>')
def greeting(name=None):
    data = ['Hello', 'World', 'Flask', 'Python']
    return render_template('demo.html', name=name, data=data)

@app.route('/my_data')
@app.route('/my_data/<string:name>')
@app.route('/my_data/<string:name>/<int:age>')
@app.route('/my_data/<string:name>/<int:age>/<int:height>')
def my_data(name=None, age=None, height=None):
    page_name = "MyData"
    dict_data = {
        'name': name,
        'age': age,
        'height': height
    }
    return render_template('my_data.html', page_name=page_name, dict_data=dict_data)