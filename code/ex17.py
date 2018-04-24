################################################
# File Name: ex17.py
# Author: ending19
# mail: ending19@163.com
# Created Time: Tue 24 Apr 2018 06:28:44 PM CST
#======================================
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists          # 用于判断文件是否存在

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line too, how?
file_input = open(from_file,'r')    # 以只读的方式打开文件
indata = file_input.read()          # 读出文件，将字符串存在indata中

print("The input file is %d bytes long" % len(indata) ) # 获取字符串长度
print("Does the output file exist? %r" % exists(to_file))# 判断文件是否存在
print("Ready, hit RETURN to continue, CTRL-C to abort")
input()

output = open(to_file, 'w')         # 以可写方式打开文件
output.write(indata)                # 写入文件

print("Alright, all done.")

output.close()
file_input.close()
