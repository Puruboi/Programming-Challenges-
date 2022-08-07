# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 10:23:19 2021

@author: PURUBOI
"""

def compareTriplets(a, b):
    alice=0
    bob=0
    # Write your code here
    for i in range(len(a)):
        if a[i]>b[i]:
            alice+=1
        if a[i]<b[i]:
            bob+=1
    return alice,bob
