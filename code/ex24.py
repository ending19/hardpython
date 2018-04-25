################################################
# File Name: ex24.py
# Author: ending19
# mail: ending19@163.com
# Created Time: Wed 25 Apr 2018 02:26:59 PM CST
#======================================
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n\
newlines and \t tabs')  # 字符串不能分两行写，除非是使用续行符'\'(原文无)

print('''You\'d need to know \'bout escapes with \\ that do
newlines and \t tabs''')        # 使用三引号也可以,不过得删除后面的'\n'

print('You\'d need to know \'bout escapes with \\ that do \n'+
'newlines and \t tabs') # 或者分成2个字符串('+'可省略)，同一组括号可跨行

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is  none.
"""

print("----------------")
print(poem)
print("----------------")

five = 10 -2 + 3 - 6
print("This should be five: %s"  % five)


def secret_formula(started):
    jelly_beans = started * 500
    jars =jelly_beans // 1000       # 在2.x中的/即为3.x中的//(地板除)
    creates = jars // 100
    return jelly_beans, jars, creates   # 返回一个元组，有3个值


start_point = 10000
beans, jars, creates = secret_formula(start_point)  # 元组多重赋值

print("With a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d creates." %
        (beans, jars, creates))     # 在同一组括号中可以换行


start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d creates." %
        secret_formula(start_point))# 将函数返回的元组中的值依次赋给占位符


