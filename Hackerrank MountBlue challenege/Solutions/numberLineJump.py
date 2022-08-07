# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 20:40:01 2021

@author: PURUBOI
"""

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if (x2>x1 and v2>v1):
        return "NO"
    a = x1+v1+x2+v2
    while a>0:
        x1=x1+v1
        x2=x2+v2
        
        if x1==x2:
            return "YES"
        a-=1
    return "NO"