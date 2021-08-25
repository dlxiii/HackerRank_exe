#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:10:10 2021

@author: yulong
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxSubarrayValue' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cal(list):
    odd=0
    eve=0
    for i in range(len(list)):
        if i%2==1:
            odd +=list[i]
        else:
            eve +=list[i]
    return (odd-eve)**2

def maxSubarrayValue(arr):
    # Write your code here
    lists=[]
    sum=[]
    for i in range(len(arr)+1):
        for j in range(i):
            lists.append(arr[j:i])
    for k in lists:
        sum.append(cal(k))
    return max(sum)
        

if __name__ == '__main__':
    
    n = int(input())
    
    arr = [int(input()) for _ in range(n)]
    
    result = maxSubarrayValue(arr)