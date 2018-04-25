################################################
# File Name: ex25.py
# Author: ending19
# mail: ending19@163.com
# Created Time: Wed 25 Apr 2018 04:02:06 PM CST
#======================================
# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def break_words(stuff):
    """This function will break up workds for us."""
    words = stuff.split(' ')    # 通过指定分隔符对字符串进行切片，默认为所有
    return words                # 空字符，此处设置为空格


def sort_words(words):
    """Sorts the words."""
    return sorted(words)        # 对可迭代的对象进行排序，返回一个新的列表


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)         # 删除列表里的第一个元素，并打印该元素
    print(word)


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)        # 删除列表里的最后一个元素，并打印该元素
    print(word)


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)# 将句子分割成单词，并返回一个排序好的列表
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of sentence."""
    words = break_words(sentence)
    print_first_word(words)     # 打印一个句子中的第一个和最后一个单词
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence) # 先将一个句子的单词进行排序
    print_first_word(words)         # 然后打印出排序后的第一个和最后一个单词
    print_last_word(words)


print(dir())        # 在import该模块时，显示该模块里的函数及方法，原文无
