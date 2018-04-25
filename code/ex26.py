################################################
# File Name: ex26.py
# Author: ending19
# mail: ending19@163.com
# Created Time: Wed 25 Apr 2018 06:50:02 PM CST
#======================================
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 原代码来自于 http://learnpythonthehardway.org/exercise26.txt
# 本代码是在原代码的基础上进行修改

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):            # 少了个冒号
    """Prints the first word after popping it off."""
    word = words.pop(0)                 # pop方法名字打错
    print(word)                         # 在python3.x中print需要带括号

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)                # 缺了右半边括号')'
    print(word)                         # 在2.x中没错，在3.x要加括号

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print("Let's practice everything.")         # 3.x,后面就不指出print的问题了
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \ttabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 5
print("This should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans // 1000      # 此处的地板除，除号应为'/',在3.x中为//
    crates = jars // 100                # 地板除为//
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)# 赋值号为'=',变量名写错

print("With a starting point of: %d" % start_point)
print("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point // 10         # 原含义是要地板除，故要更改

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point))                              # 变量名写错，缺少括号


sentence = "All god\tthings come to those who weight."

words = break_words(sentence)           # 在模块内部调用函数不用加上模块名
sorted_words = sort_words(words)        # 删除'ex25.'

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)          # 在模块内部调用函数不用加上'.'
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)
print(sorted_words)                     # print函数写错

print_first_and_last(sentence)          # 函数名写错

print_first_and_last_sorted(sentence)    # 不能随意缩进，且变量和函数名写错
