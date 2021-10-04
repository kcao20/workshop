# Yoonah Chang, Michael Borczuk, Kevin Cao (Team Sneakers)
# SoftDev
# K06 -- StI/O: Divine your Destiny!
# 2021-09-28

'''
Our Approach
We decided to split the problem into two parts: reading the csv file
and finding/printing the job. We decided to use csv module to construct
our dictionary. While creating this dictionary, we multiplied each
percentage by 10, since each percentage only went out to one decimal
place. This allowed us to work with integers. To find the job, we
generated a random integer from 0 to 999 (inclusive), and then checked
to see which of the ranges we created (based on the probabilities) the
integer fell into. This seems to work quite well!
'''

import csv
import random

dict = {}

with open('occupations.csv', mode='r') as file:

    # reading the CSV file
    csvFile = csv.DictReader(file)

    # add contents to dictionary, multiply by 10 to make probabilities easier
    for lines in csvFile:
        dict[lines['Job Class']] = float(lines['Percentage']) * 10


def print_occupations():
    dict1 = dict.copy()
    dict1.pop('Total')
    return "<br />".join(dict1.keys())


def choose():

    # generate a random integer
    num = random.randint(0, 999)

    counter = 0

    # adds to counter, once it passes randomly generated number, it prints the key
    for key in dict.keys():
        if counter + dict[key] > num:
            return(key)
            # exit loop once we've found our job
            break
        else:
            counter += dict[key]
            # continue to next iteration so we don't print Jobless every time
            continue
        # if the random int doesn't fall within any range, there is no job
        return("Other Job")
