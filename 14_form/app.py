# Team The Best Laptop - Jonathan W. [Loki] , Alif A. [The Eagle in the Sand], Kevin C. [Pipi] | Period 2
# SoftDev
# K14 - Form and Function/Observing forms in html/We investigated requests and responses in html files and how it related to flask & jinja as well as the function of the code to learn from it for future uses.
# 2021-10-14

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
    #print("***DIAG: request.args['username']  ***")
    # print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template('login.html')


@app.route("/auth")
def response():
    user = request.args['username']
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #print("***DIAG: request.args['username']  ***")
    # print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template("response.html", username=user, request_method=request.method)


if __name__ == "__main__":
    app.debug = True
    app.run()
