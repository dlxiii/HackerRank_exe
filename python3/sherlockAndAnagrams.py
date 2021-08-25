#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 23:53:02 2021

@author: yulong

给定一个字符串，找出无序 变形子串对的数目。

Input Format

第一行包含，测试数据的组数。 每组测试数据是在在一行中的字符串。

约束条件

的
长
度

Output Format

对每组测试数据，在一行中输出要求的答案。

Sample Input 0

2
abba
abcd
Sample Output 0

4
0
Explanation 0

The list of all anagrammatic pairs is  and  at positions  and  respectively.

No anagrammatic pairs exist in the second query as no character repeats.

Sample Input 1

2
ifailuhkqq
kkkk
Sample Output 1

3
10
Explanation 1

For the first query, we have anagram pairs  and  at positions  and  respectively.

For the second query:
There are 6 anagrams of the form  at positions  and .
There are 3 anagrams of the form  at positions  and .
There is 1 anagram of the form  at position .

Sample Input 2

1
cdcd
Sample Output 2

5
Explanation 2

There are two anagrammatic pairs of length :  and .
There are three anagrammatic pairs of length :  at positions  respectively.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    d={}
    res=0
    for i in range(1,len(s)):
        for j in range(len(s)-i+1):
            subs = ''.join(sorted(s[j:j+i]))
            if subs not in d:
                d[subs]=1
            else:
                d[subs]+=1
            res+=d[subs]-1
    return res
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
