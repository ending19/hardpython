################################################
# File Name: ex7.py
# Author: ending19
# mail: ending19@163.com
# Created Time: Tue 24 Apr 2018 02:30:53 PM CST
#======================================
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Mary had a little lamb.")
print("Its fleece was white as %s." % 'snow')
print("And everywhere that Mary went.")
print("." * 10)             # what'd that do?

end1 = 'C'
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

# watch that comma at the end. Try removing it to see what happens  -- 2.x
# add ,end='' in the print function, try it and to see what happens --3.x

# print end1 + end2 + end3 + end4 + end5 + end6,    # this is for python2.x
# print end7 + end8 + end9 +end10 + end11 + end12
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')# Here is a space
print(end7 + end8 + end9 +end10 + end11 + end12)
