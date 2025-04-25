# RUN APP
# flask --app .\src\HelloWorld\Hello.py run
# flask --app .\src\HelloWorld\Hello.py --debug run

from flask import Flask

app = Flask(__name__)

# Ruta unica
@app.route('/HelloWorld')
def hello_page():
    return "<b> Hello, World!"

# Doble ruta
@app.route('/')
@app.route('/Main')
def main_page():
    return "Main Page"

# Ruta con variable
# int
# str
# float
# path
# uuid
# date
# time
# datetime

@app.route('/Hi')
@app.route('/Hi/<name>')
@app.route('/Hi/<name>/<int:age>')
def hi_page(name=None, age=None):
    
    if name is None and age is None:
        return "Hi unknown user"
    
    if age is None:
        return f"Hi {name}"
    else:
        return f"<H1>Hi {name}</H1><br><H2>Your age {age}<H2>"


from markupsafe import escape
@app.route('/code/<path:code>')
def code_page(code):
    return f"Code: <br>{escape(code)}"