### Buikding URL dynamically
### variable rule
### jinja 2  template engine

from flask import Flask, render_template,request,redirect,url_for

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



## variable rule 
@app.route("/success/<int:score>")
def success(score):
    return f"Congratulations, {score}." + str(score)

@app.route("/marks/<int:score>")
def marks(score):
    res = ""
    if score >= 55:
        res = "You have passed"
    else:
        res = "You have failed"
    return render_template("result.html",results=res)

@app.route("/forloop/<int:score>")
def forloop(score):
    res = ""
    if score >= 55:
        res = "You have passed"
    else:
        res = "You have failed"
    exp = {'Score' : score, 'Result' : res}

    return render_template("forloop.html",results=exp)

@app.route("/marksif/<int:score>")
def marksif(score):
    
    return render_template("resultif.html",results=score)

@app.route("/submit", methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
            science = float(request.form['science'])
            maths = float(request.form['maths'])
            c = float(request.form['c'])
            data_science = float(request.form['datascience'])

            total = (science + maths + c + data_science) / 4
            return redirect(url_for('forloop', score=total))
        except ValueError:
            return "Invalid input! Please enter numeric values."

    # If it's a GET request, render the form
    return render_template("getresult.html")



@app.route("/Home")
def home():
    return "Welcome to the Home"

if __name__ == '__main__':
    app.run(debug=True)