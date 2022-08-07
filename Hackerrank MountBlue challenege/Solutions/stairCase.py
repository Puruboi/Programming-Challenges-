# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 21:02:48 2021

@author: PURUBOI
"""
n=5
def staircase(n):
    # Write your code here
    for i in range(n):
        for j in range(n):

            if i+j==n-1 or i==n-1 or j==n-1 or i+j>=n:
                print('#',end="")
            else:
                print(" ",end="")
        print()
        
staircase(n)
    