from flask import Flask
'''
It creates a new instance of the Flask class , 
which will be your WSGI(Web Server Gateway Interface) application'''
### WSGI Application
app = Flask(__name__)

@app.route("/")

def welcome():
    return "Welcome to the Flask World!"

@app.route("/index")

def index():
    return "Welcome to the Index Page"

@app.route("/home")

def home():
    return "Welcome to the home Page"

if __name__ == '__main__':
    app.run(debug=True)