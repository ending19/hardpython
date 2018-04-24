################################################
# File Name: ex16.py
# Author: ending19
# mail: ending19@163.com
# Created Time: Tue 24 Apr 2018 05:03:16 PM CST
#======================================
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv         # 传入要操作的文件

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C(^C).")
print("If you do want that, hit RETURN.")

input('?')

print("Opening the file...")
target = open(filename, 'w')    # 以可写的方式打开文件

print("Truncating the file. Goodbye!")
target.truncate()               # 清空文件

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1+'\n'+line2+'\n'+line3+'\n')  # 向文件写入字符串

print("And finally, we close it.")
target.close()          # 关闭文件
