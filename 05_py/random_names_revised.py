# Kevin Cao, Raymond Yeung, Yaying Liang Li
# Software Development
# K02 -- Python Random Name Generator - Amalgamation
# 2021-09-24
# ----------------------------------------------------------------------------
# Pow-Wow Summary
# Discovery: Adding to a text file is way easier than adding to a list
# Question:  How much do we have to comment our code?
#            How much does runtime/efficiency matter?
# Comments:  Combining code is pretty fun

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
