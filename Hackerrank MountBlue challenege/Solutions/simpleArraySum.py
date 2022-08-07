# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 08:02:27 2021

@author: PURUBOI
"""
def simpleArraySum(ar):
    # Write your code here
    def sumArray(ar):
        res=0
        for i in ar:
            res+=i
        return res
    return sumArray(ar)

ar_count = int(input().strip())
ar = list(map(int, input().rstrip().split()))
result = simpleArraySum(ar)
print(result)

