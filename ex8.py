################################################
# File Name: ex8.py
# Author: ending19
# mail: ending19@163.com
# Created Time: Tue 24 Apr 2018 02:47:56 PM CST
#======================================
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

formatter = "%r %r %r %r"           # %r是打印任意格式的字符,调用的是rper()
                                    # %s是调用了str()
print(formatter % (1, 2, 3, 4))
print(formatter % ('one', 'two', 'three', 'four'))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
    ))
