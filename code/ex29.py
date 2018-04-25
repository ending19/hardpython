################################################
# File Name: ex29.py
# Author: ending19
# mail: ending19@163.com
# Created Time: Wed 25 Apr 2018 09:15:41 PM CST
#======================================
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")
