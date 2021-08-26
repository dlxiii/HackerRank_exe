#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 01:12:15 2021

@author: yulong

You are given an array and you need to find number of tripets of indices  such that the elements at those indices are in geometric progression for a given common ratio  and .

Example
 

There are  and  at indices  and . Return .

Function Description

Complete the countTriplets function in the editor below.

countTriplets has the following parameter(s):

int arr[n]: an array of integers
int r: the common ratio
Returns

int: the number of triplets
Input Format

The first line contains two space-separated integers  and , the size of  and the common ratio.
The next line contains  space-seperated integers .

Constraints

Sample Input 0

4 2
1 2 2 4
Sample Output 0

2
Explanation 0

There are  triplets in satisfying our criteria, whose indices are  and 

Sample Input 1

6 3
1 3 9 9 27 81
Sample Output 1

6
Explanation 1

The triplets satisfying are index , , , ,  and .

Sample Input 2

5 5
1 5 5 25 125
Sample Output 2

4
Explanation 2

The triplets satisfying are index , , , .
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    bef = dict()
    aft = dict()
    count=0
    for val in arr:
        if val in aft:
            aft[val] += 1
        else:
            aft[val] = 1
            
    for val in arr:
        aft[val] -= 1
        if val // r in bef and val * r in aft and val % r == 0:
            count += bef[val//r] * aft[val*r]
        if val in bef:
            bef[val] += 1
        else:
            bef[val] = 1
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
