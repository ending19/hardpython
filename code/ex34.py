################################################
# File Name: ex34.py
# Author: ending19
# mail: ending19@163.com
# Created Time: Thu 26 Apr 2018 03:27:19 PM CST
#======================================
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 这是一个测试代码，用于检查答案

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platpus']

test = ["1. The animal at 1.",
        "2. The 3rd animal.",
        "3. The 1st animal.",
        "4. The animal at 3.",
        "5. The 5th animal.",
        "6. The animal at 2.",
        "7. The 6th animal.",
        "8. The animal at 4."
        ]

cardinal = ['0', '1', '2', '3', '4', '5', '6']
ordinal = ['1st','2nd','3rd','4th','5th','6th']



print("Press RETURN to check your answer.")

for x in test:
    nums = cardinal[1:]
    if x[7] in nums:
        index = int(x[7]) - 1
        print(x,end='')
        input()
        print(x[3:len(x)-1],"is at",cardinal[index],"and is a",animals[index]+'.')
    else:
        index = int(x[-2])
        print(x,end='')
        input()
        print(x[3:len(x)-1],"is the",ordinal[index],"and is a",animals[index]+'.')

