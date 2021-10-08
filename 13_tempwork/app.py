# Team PPS: Kevin Cao (Pipi), Thomas Yu (Perry), Han Zhang(Sirap)
# SoftDev
# K13: Template for Success
# 2021-10-8

from flask import Flask, render_template
import random
import csv


app = Flask(__name__)  # create instance of class Flask

@app.route("/occupyflaskst")  # assign fxn to route

def main():
    dict = {}
    with open("data/occupations.csv", mode = 'r') as csvfile:
        file = csv.DictReader(csvfile)

        for lines in file:
            dict[lines['Job Class']] = float(lines['Percentage'])

    return render_template( 'tablified.html', title='K13', heading=heading(), occupations=dict, occupation=randomoccupation() )

def heading():
    return "Team PPS: Kevin Cao (Pipi), Thomas Yu (Perry), Han Zhang(Sirap)"


def randomoccupation():
    randomNum = random.random()* 99.8
    dict = {}

    with open("data/occupations.csv", mode = 'r') as csvfile:
        file = csv.DictReader(csvfile)

        for lines in file:
            dict[lines['Job Class']] = float(lines['Percentage'])

    x = 0.0
    for i, j in dict.items():
        if x <= randomNum < x + j:
            return ("Your occupation is: " + i)
            break
        x += j

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
