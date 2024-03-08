from flask import Flask, render_template

#flask instance 
app = Flask(__name__)

# create a route decorator 

@app.route('/')
def index():
    first_name= "paapi"
    fthings=["1","adhd","bka",1]
    stuff = "This is <strong>faltugiri</strong> gg "
    return render_template("index.html",
                           first_name=first_name
                           ,stuff=stuff,
                           fthings=fthings)
#http://127.0.0.1:5000/user/death
@app.route('/user/<name>')
def user(name):
    return render_template("user.html",user_name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("404.html"),505