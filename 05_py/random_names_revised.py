# Kevin Cao, Raymond Yeung, Yaying Liang Li
# Software Development
# K05 -- Python Random Name Generator - Amalgamation
# 2021-09-24
# ----------------------------------------------------------------------------
# Summary of Trio Discussion
# We discussed whether we wanted our user to choose which period the names
# came from, and we made an executive decision in the end not to prompt the
# user for a period. Instead, we decided that the program would randomly
# choose a name from any period - as Kevin said, a "truly random" program.
#
# Discoveries
# If we did prompt the user to enter a period, we'd need some conditional
# in case the user typed in a period without a roster
#
# Questions
# What are the benefits of storing the names with a dictionary as opposed to
# with a .txt file?
#
# Comments
# random.randint(a,b) is inclusive on both ends - and since indexes start at 0,
# that's why the endpoint has to have -1

import random


names = {
    'pd1': ["Owen Yaggy", "Haotian Gan", "Ishraq Mahid", "Ivan Lam",
            "Michelle Lo", "Christopher Liu", "Ivan Mijacika", "Lucas Lee",
            "Josephine Lee", "Rayat Roy", "Emma Buller", "William Chen",
            "Rachel Xiao", "Andrew Juang", "Yuqing Wu", "Renggeng Zheng",
            "Annabel Zhang", "Alejandro Alonso", "Deven Maheshwari",
            "Oscar Wang", "Tami Takada", "Yusuf Elsharawy", "Ella Krechmer",
            "Tomas Acuna", "Tina Nguyen", "Theo Fahey", "Sadid Ethun"],
    'pd2': ["Patrick Ging", "Wenhao Dong", "Raymond Yeung", "Kevin Cao",
            "Michael Borczuk", "Alif Abdullah", "Justin Zou", "Andy Lin",
            "Shadman Rakib", "David Chong", "Daniel Sooknanan",
            "Cameron Nelson", "Austin Ngan", "Yaying Liang Li", "Eric Guo",
            "Noakai Aronesty", "Roshani Shrestha", "Yoonah Chang", "Qina Liu",
            "Han Zhang", "Joshua Kloepfer"]
}

# Find length of each list
pd1_len = len(names['pd1'])
pd2_len = len(names['pd2'])

# Choose a random person
num = random.randint(0, pd1_len + pd2_len - 1)
if num < pd1_len:
    print("period 1: " + names['pd1'][num])
else:
    print("period 2: " + names['pd2'][num - pd1_len])
