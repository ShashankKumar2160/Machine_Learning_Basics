from flask import Flask,render_template
'''
It creates a new instance of the Flask class , 
which will be your WSGI(Web Server Gateway Interface) application'''
### WSGI Application
app = Flask(__name__)

@app.route("/")

def welcome():
    return "<html><H1>Welcome To the Flask Course!</H1></html"

@app.route("/index")

def index():
    return render_template("index.html")

@app.route("/home")

def home():
    return "Welcome to the home Page"

@app.route("/about")

def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)