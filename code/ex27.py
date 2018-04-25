################################################
# File Name: ex27.py
# Author: ending19
# mail: ending19@163.com
# Created Time: Wed 25 Apr 2018 07:25:15 PM CST
#======================================
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 该节用于记忆逻辑式的真假，此处代码仅用于方便测试

# NOT
a = not False
b = "not False"
print(b,"?", end='\t\t\t')
input()
print(a)
a = not True
b = "not True"
print(b,"?", end='\t\t\t')
input()
print(a)

# OR
a = True or False
b = "True or False"
print(b,"?", end='\t\t\t')
input()
print(a)
a = True or True
b = "True or True"
print(b,"?", end='\t\t\t')
input()
print(a)
a = False or True
b = "False or True"
print(b,"?", end='\t\t\t')
input()
print(a)
a = False or False
b = "False or False"
print(b,"?", end='\t\t')
input()
print(a)

# AND
a = True and False
b = "True and False"
print(b,"?", end='\t\t')
input()
print(a)
a = True and True
b = "True and True"
print(b,"?", end='\t\t\t')
input()
print(a)
a = False and True
b = "False and True"
print(b,"?", end='\t\t')
input()
print(a)
a = False and False
b = "False and False"
print(b,"?", end='\t\t')
input()
print(a)

# NOT OR
a = not (True or False)
b = "not (True or False)"
print(b,"?", end='\t\t')
input()
print(a)
a = not (True or True)
b = "not (True or True)"
print(b,"?", end='\t\t')
input()
print(a)
a = not (False or True)
b = "not (False or True)"
print(b,"?", end='\t\t')
input()
print(a)
a = not (False or False)
b = "not (False or False)"
print(b,"?", end='\t\t')
input()
print(a)

# NOT AND
a = not (True and False)
b = "not (True and False)"
print(b,"?", end='\t\t')
input()
print(a)
a = not (True and True)
b = "not (True and True)"
print(b,"?", end='\t\t')
input()
print(a)
a = not (False and True)
b = "not (False and True)"
print(b,"?", end='\t\t')
input()
print(a)
a = not (False and False)
b = "not (False and False)"
print(b,"?", end='\t\t')
input()
print(a)

# !=
a = (1 != 0)
b = "1 != 0"
print(b,"?", end='\t\t\t')
input()
print(a)
a = (1 != 1)
b = "1 != 1"
print(b,"?", end='\t\t\t')
input()
print(a)
a = (0 != 1)
b = "0 != 1"
print(b,"?", end='\t\t\t')
input()
print(a)
a = (0 != 0)
b = "0 != 0"
print(b,"?", end='\t\t\t')
input()
print(a)

# ==
a = (1 == 0)
b = "1 == 0"
print(b,"?", end='\t\t\t')
input()
print(a)
a = (1 == 1)
b = "1 == 1"
print(b,"?", end='\t\t\t')
input()
print(a)
a = (0 == 1)
b = "0 == 1"
print(b,"?", end='\t\t\t')
input()
print(a)
a = (0 == 0)
b = "0 == 0"
print(b,"?", end='\t\t\t')
input()
print(a)
