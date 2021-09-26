# Kevin Cao
# SoftDev
# K02 -- Python Random Name Generator - Amalgamation
# 2021-09-24

import random

if __name__ == '__main__':
    # Create list for each period
    pd1 = []
    pd2 = []

    # Fill each list from text file
    with open("pd1.txt", 'r') as file:
        for line in file:
            pd1.append(line.rstrip('/n'))

    with open('pd2.txt', 'r') as file:
        for line in file:
            pd2.append(line.rstrip('/n'))

    # Find length of each list
    pd1_len = len(pd1)
    pd2_len = len(pd2)

    # Test to see if either list is empty
    if pd1_len < 1 or pd2_len < 1:
        print("Lists are empty")

    # Choose a random person
    num = random.randint(0, pd1_len + pd2_len - 1)
    if num < pd1_len:
        print("period 1: " + pd1[num])
    else:
        print("period 2: " + pd2[num - pd1_len])
