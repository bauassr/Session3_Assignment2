# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 15:17:56 2018

@author: singh.shivam
"""

s="Acadgild"
result1=[x  for x in s]    
print(result1)
s="XYZ"
result02 =[x*i for x in s for i in range(1,5) ]
print(result02)
result03 =[x*i for i in range(1,5) for x in s ]
print(result03)
result04=[[a]  for i in range(2,7) for a in range(i,i+3)]  
print(result04)
result2=[[a,b,c]  for i in range(2,6) for a in range(i,i+1)
 for b in range(a+1,a+2) for c in range(b+1,b+2)]  
print(result2)

result3=[(y,x) for x in range(1,4) for y in range(1,4)]
print(result3)

