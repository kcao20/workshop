# Team Sneakers: Yoonah Chang (Yelena), Kevin Cao (Pipi), Michael Borczuk (Liberty and Baby Yoda)
# SoftDev
# K10 -- Putting Little Pieces Together
# 2021-10-04

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()

'''
It is the same as v2, but it turns the debugger on.
'''