from projet import app
from flask import render_template

app.secret_key = "0x131F824"
app.config['PERMANENT_SESSION_LIFETIME'] = 3600


@app.errorhandler(404)
def page_not_found(e):
    data = {
        "title": "Hello World",
        "body": "Flask simple MVC"
    }
    return {'message':'Not found error'}



@app.errorhandler(Exception)
def exception_handler(error):
    return "!!!!"  + repr(error)
