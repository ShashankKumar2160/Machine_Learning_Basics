from flask import Flask, render_template,request

'''
   It creates a new instance of Flask class,
   which will be your WSGI(Web Server Gateway Interface) application.
'''
### WSGI Application
app = Flask(__name__)

@app.route("/")
def Welcome():
    return "<html><H1>Welcome to the Flask Course</H1></html>"

@app.route("/index",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form",methods=["GET", "POST"])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}!"
    return render_template("form.html")

@app.route("/submit",methods=["GET", "POST"])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}!"
    return render_template("form.html")

@app.route("/Home")
def home():
    return "Welcome to the Home"

if __name__ == '__main__':
    app.run(debug=True)