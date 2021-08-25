#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 23:26:52 2021

@author: yulong

给你两个字符串和，找出是否存在一个字符串同时出现在和中。

Input Format

一个文件中将给你一些测试数据。输入的第一行将包含一个整数，测试数据组数。

然后将有组测试数据的描述。 每个描述包含两行，第一行包含字符串，第二行包含字符串。

Output Format

对每组测试数据，如果有公共子串，输出 "YES"。如果没有公共子串，输出"NO"。

Sample Input

2
hello
world
hi
world
Sample Output

YES
NO
Explanation

约束条件

所有的字符串只包含小写字母。



"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    # Write your code here
    if set(s1)&set(s2):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
