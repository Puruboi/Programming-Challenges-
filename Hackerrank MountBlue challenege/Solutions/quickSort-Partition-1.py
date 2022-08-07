# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 10:23:19 2021

@author: PURUBOI
"""

def quickSort(arr):
    # Write your code here
    p=arr[0]
    l,e,r=[],[],[]
    for i in range(len(arr)):
        if arr[i]<p:
            l.append(arr[i])
        if arr[i]>p:
            r.append(arr[i])
        if arr[i]==p:
            e.append(arr[i])
    return l+e+r