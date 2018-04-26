################################################
# File Name: ex30.py
# Author: ending19
# mail: ending19@163.com
# Created Time: Thu 26 Apr 2018 02:00:07 PM CST
#======================================
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

people = 30
cars = 40
buses = 15


if cars > people:               # 如果车比人多
    print("We should take the cars.")
elif cars < people:             # 在前面条件不满足的情况下，如果车比人少
    print("We should not take the cars.")
else:                           # 之前的情况都不满足
    print("We can't decide.")

if buses > cars:
    print("That's too many buses.")
elif buses < cars:
    print("Maybe we could take the buses.")
else:
    print("We still can't decide.")

if people > buses:
    print("Alright, let's just take the buses.")
else:
    print("Fine, let's stay home then.")


