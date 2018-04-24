################################################
# File Name: ex13.py
# Author: ending19
# mail: ending19@163.com
# Created Time: Tue 24 Apr 2018 04:05:54 PM CST
#======================================
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv        # 导入sys模组的argv功能，argv为传入的参数变量

script, first, second, third = argv # 将argv解包(unpack)并依次赋值给左边变量

print("The script is called:", script)
print("Your first variale is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

