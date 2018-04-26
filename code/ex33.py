################################################
# File Name: ex33.py
# Author: ending19
# mail: ending19@163.com
# Created Time: Thu 26 Apr 2018 02:58:38 PM CST
#======================================
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

i = 0
numbers = []

while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)
    i = i + 1
    print("Numbers now: ", numbers)
    print("At the bottom i is %d" % i)


print("The numbers: ")

for num in numbers:
    print(num)

# 函数实现
def whileloop(stop, step):
    i = 0
    numbers = []
    while i < stop:
        print("At the top i is %d" % i)
        numbers.append(i)
        i = i + step
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)
    return numbers

print("The numbers: ")

for num in whileloop(6,1):
    print(num)
