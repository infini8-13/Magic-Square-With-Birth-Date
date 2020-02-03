"""
Created on Thu Dec  5 18:20:40 2019

@author: infini8
"""

import numpy as np


print("Enter name ,then your birthday in the format(DD MM YY YY)")
name=input()
n = [int(x) for x in input().split(' ')]
r1=[n[0],n[1],n[2],n[3]]
r2=[n[3]+1,n[2]-1,n[1]-3,n[0]+3]
r3=[n[1]-2,n[0]+2,n[3]+2,n[2]-2]
r4=[n[2]+1,n[3]-1,n[0]+1,n[1]-1]
magic_s=np.array([r1,r2,r3,r4])
print("Your personalised Magic Matrix!")
print(name+str('\'s Magic Matrix'))
print(magic_s)
