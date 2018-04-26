################################################
# File Name: ex32.py
# Author: ending19
# mail: ending19@163.com
# Created Time: Thu 26 Apr 2018 02:30:43 PM CST
#======================================
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']


# this first kind of for-loop goes through a list   遍历一个列表
for number in the_count:
    print("This is count %d" % number)


# same as above
for fruit in fruits:
    print("A fruit of type: %s" % fruit)


# also we can go through mixed lists too
# 列表支持混合类型，既可以有数字也可以有字符串
# notice we have to use %r since we don't know what's in it
# 当我们不知道列表里的类型时，可以使用'%r'
for i in change:
    print("I got %r" % i)


# we can also build lists, first start with an empty one    可以创建空列表
elements = []


# then use the range function to de 0 to 5 counts
for i in range(0, 6):           # range函数生成的，包括左边元素，不包含右边
    print("Adding %d to the list." % i)
    # append is a function that lists understand
    elements.append(i)          # append方法用于在列表结尾添加元素


# now we can print them out too
for i in elements:
    print("Element was: %d" % i)


# 另外的内容
elements = range(0, 6)  # 在3.x中的range是2.x中xrange，生成的不再是一个列表
print(elements)         # 而是一个生成器，若要生成列表，需要调用list()函数
print("%s" % elements)  # 3.x中无xrange()
print("%r" % elements)

elements = list(range(0, 6))
print(elements)
print("%s" % elements)
print("%r" % elements)
