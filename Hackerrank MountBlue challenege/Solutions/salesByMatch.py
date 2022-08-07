# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 19:38:30 2021

@author: PURUBOI
"""

def sockMerchant(n, ar):
    # Write your code here
    def count(l):
        a=dict()
        for i in l:
            c=0
            for j in l:

                if i==j:
                    c+=1
            a[i]=c
        return a

    def pairing(ar):

        c=count(ar)
        d=0
        for i in c.values():
            if ((i//2)>0):
                d+=(i//2)
        return d

    return pairing(ar)

n = int(input().strip())
ar = list(map(int, input().rstrip().split()))
result = sockMerchant(n, ar)
print(result)

    
    
    

    
    
    
        
        