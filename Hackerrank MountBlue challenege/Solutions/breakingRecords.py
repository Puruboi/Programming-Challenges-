# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 08:11:23 2021

@author: PURUBOI
"""

def breakingRecords(scores):
    def highRecord(ar):
        ar=ar 
        a=ar[0]
        c=0

        for i in ar:
            if a<i:
                c+=1
                a=i
        return c

    def leastRecord(ar):
        ar=ar
        b=ar[0]
        d=0

        for j in ar:
            if b>j:
                d+=1
                b=j
        return d

    def highleastcount(ar):

        h=highRecord(ar)
        l=leastRecord(ar)
        return (h,l)
    return highleastcount(scores)


n = int(input().strip())  # size of array

scores = list(map(int, input().rstrip().split())) #array

result = breakingRecords(scores)

print(result)
