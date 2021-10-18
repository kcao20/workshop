# Team The Best Laptop - Jonathan W. [Loki] , Alif A. [The Eagle in the Sand], Kevin C. [Pipi] | Period 2
# SoftDev
# K15 - Sessions Greetings/More form handling in HTML in flask app/We worked on creating a flask app that uses session capabilities to allow a user to login and logout.
# 2021-10-18

from flask import Flask             # facilitate flask webserving
from flask import render_template   # facilitate jinja templating
from flask import request           # facilitate form submission
app = Flask(__name__)


@app.route("/")  # , methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template('login.html')


@app.route("/auth")
def response():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.headers ***")
    print(request.headers)
    user0 = 'kevinjonleafy'
    passw0 = 'dellthebestlaptop15'
    error = ""
    user = ""
    passw = ""
    if request.method == 'GET':
        user = request.args['username']
        passw = request.args['password']
    else request.method == 'POST':
        user = request.form['username']
        passw = request.form['password']
    if user0 != user and passw0 != passw:
        error = "uer and pass wrong"
    try:
        return render_template("response.html", username=user, password=passw)
    except:
        return render_template("login.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
