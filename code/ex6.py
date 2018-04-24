################################################
# File Name: ex6.py
# Author: ending19
# mail: ending19@163.com
# Created Time: Tue 24 Apr 2018 02:18:50 PM CST
#======================================
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)

print("I said: %r." % x)
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."
print(w + e)        # '+'可以拼接字符串



