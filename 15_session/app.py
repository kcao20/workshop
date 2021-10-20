# Team The Best Laptop - Jonathan Wu [Loki] , Alif Abdullah [The Eagle in the Sand], Kevin Cao [Pipi] | Period 2
# SoftDev
# K15 - Sessions Greetings/More form handling in HTML in flask app/We worked on creating a flask app that uses session capabilities to allow a user to login and logout.
# 2021-10-18

from flask import Flask             # facilitate flask webserving
from flask import render_template   # facilitate jinja templating
from flask import request           # facilitate form submission
from flask import session           # facilitate session handling
app = Flask(__name__)

app.secret_key = "professional_secret_key"


@app.route("/")  # , methods=['GET', 'POST'])
def disp_login():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.headers ***")
    print(request.headers)
    if 'user' in session:  # checks to see if there is a session
        user = session['user']
        loadText = "Click the button below to logout."
        return render_template("response.html", username=user, request_method=request.method, message=loadText)
    else:  # return login page
        landingText = "Enter your username below to proceed."
        return render_template('login.html', message=landingText)


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
    user0 = 'a'
    passw0 = 'b'
    loadText = ""
    user = ""
    passw = ""
    if 'user' in session:  # checks to see if there is a session, if there is show response page
        user = session['user']
        loadText = "Click the button below to logout."
        return render_template("response.html", username=user, request_method=request.method, message=loadText)
    else:  # check for any username/password errors
        if request.method == 'GET':
            user = request.args['username']
            passw = request.args['password']
        elif request.method == 'POST':
            user = request.form['username']
            passw = request.form['password']
        if user0 != user and passw0 != passw:
            loadText = "Could not log in. User and password wrong."
            return render_template("login.html", message=loadText)
        elif user0 != user and passw0 == passw:
            loadText = "Could not log in. User is wrong."
            return render_template("login.html", message=loadText)
        elif user0 == user and passw0 != passw:
            loadText = "Could not log in. Password is wrong."
            return render_template("login.html", message=loadText)
        else:  # if username and password match, show response page
            session['user'] = user
            loadText = "Click the button below to logout."
            return render_template("response.html", username=user, request_method=request.method, message=loadText)


@app.route("/logout")
def logoutSession():
    landingText = "You've logged out. Enter your login credentials below to proceed. "
    session.pop('user', None)
    return render_template("login.html", message=landingText)


if __name__ == "__main__":
    app.debug = True
    app.run()
