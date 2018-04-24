################################################
# File Name: ex20.py
# Author: ending19
# mail: ending19@163.com
# Created Time: Tue 24 Apr 2018 08:01:00 PM CST
#======================================
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv

script, input_file = argv


def print_all(f):
    '打印整个文件'
    print(f.read())

# seek方法用于移动文件读取指针到指定位置,
# offset : 开始的偏移量，也就是代表需要移动偏移的字节数
# whence :可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
def rewind(f):
    '重新定位'
    f.seek(0)           # 将文件读取指针移到开头


def print_a_line(line_count, f):    # 逐行读出f文件的每行数据，一次读取一行
    print(line_count,f.readline())


current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)                         # 打印整个文件

print("Now let's rewind, kind of like a tape.") # 倒磁带
rewind(current_file)                            #定位到开头

print("Let's print three lines:")               #打印3行数据
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)

