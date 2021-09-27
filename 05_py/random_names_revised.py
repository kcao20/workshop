# Kevin Cao, Raymond Yeung, Yaying Liang Li
# Software Development
# K02 -- Python Random Name Generator - Amalgamation
# 2021-09-24
# ----------------------------------------------------------------------------
# Pow-Wow Summary
# Discovery: Adding to a text file is way easier than adding to a list
# Question: How much do we have to comment our code?
#           How much does runtime/efficiency matter?
# Comments: Combining code is pretty fun

import random


def fill_list(file, list):
    with open(file, 'r') as file:
        for line in file:
            list.append(line.rstrip('/n'))


if __name__ == '__main__':
    # Create list for each period
    pd1 = []
    pd2 = []

    # Fill each list from text file
    fill_list('pd1.txt', pd1)
    fill_list('pd2.txt', pd2)

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
