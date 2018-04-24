################################################
# File Name: ex15.py
# Author: ending19
# mail: ending19@163.com
# Created Time: Tue 24 Apr 2018 04:41:32 PM CST
#======================================
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv


script, filename = argv

txt = open(filename)

print("Here's your file %r:" % filename)
print(txt.read())               # 读取文件的内容并将其以字符串的形式返回
txt.close()                     # 完成文件操作后要记得close文件

print("Type the filename again:")
file_again = input('>')

txt_again = open(file_again)
print(txt_again.read())
txt_again.close()
