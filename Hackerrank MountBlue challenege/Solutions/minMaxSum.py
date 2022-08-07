# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 15:11:36 2021

@author: PURUBOI
"""
from copy import deepcopy
def recur(a,i=0,b=[]):
    if i>=n:
        return b
    a1=deepcopy(a)
    a1.remove(a1[i])
    s=0
    for j in a1:
        s+=j
    b.append(s)
    return recur(a,i+1,b)

a=[1,2,3,4,5,6]
n=len(a)
b=recur(a)
print(min(b),max(b))