# Team Sneakers: Yoonah Chang (Yelena), Kevin Cao (Pipi), Michael Borczuk (Liberty and Baby Yoda)
# SoftDev
# K10 -- Putting Little Pieces Together
# 2021-10-04

from flask import Flask
import random_occupations
app = Flask(__name__)  # create instance of class Flask


@app.route("/")  # assign fxn to route

def main():
    return heading() + "<br/>" + occupations()

def heading():
    return "<h2> Team Sneakers: Yoonah Chang (Yelena), Kevin Cao (Pipi), Michael Borczuk (Liberty and Baby Yoda) </h2>"

def occupations():
    occupations = random_occupations.print_occupations()
    occupation = "Your occupation is: " + random_occupations.choose()
    return f"<b>List of occupations:</b> <br/><br/> {occupations} <br/><br/> <b>{occupation}</b>"


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
