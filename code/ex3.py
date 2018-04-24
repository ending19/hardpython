################################################
# File Name: ex3.py
# Author: ending19
# mail: ending19@163.com
# Created Time: Tue 24 Apr 2018 01:34:06 PM CST
#======================================
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

print('I will now count my chickens:')
print("Hens", 25 + 30 // 6)     #在2.x版本下/是地板除，而在3.x中换成//
print("Roosters", 100 - 25 * 3 % 4 )    #普通的／代表浮点数的除法

print("Now I will count the eggs:")
print(3 + 2 + 1 - 5 + 4 % 2 - 1 // 4 + 6)   #地板除//即，去除小数部分

print("Is it true that 3 + 2 < 2 - 7?")
print( 3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)
print("Oh, that's why it's False.")

print("How about some more.")
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
