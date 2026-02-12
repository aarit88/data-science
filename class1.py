# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 19:08:28 2024

@author: binit
"""

print("welcome u all1")
'''
print("welcome u all2")
print("welcome u all3")
'''
print("welcome u all again")

x=5
y="amit chauhan"
print(x)
print(type(x))
print(y)

x=str(3)    #'3'
y=int(3)    #3
z=float(3)  #3.0

print(type(x))
print(type(y))
print(type(z))

a=200
b=20
if a>b:
    print("a is greater")
if b>a:
    print("b is greater")
    
if a>b:
    print("a1 is greater")
elif b>a:
    print("b1 is greater")
    
if a>b and a==b:
    print("a1 is greater")
elif b>a:
    print("b1 is greater")
else:
    print("they r equal")
    
i=1
while i<6:
    print(i)
    #if i==3:
       #break
    i+=1
else:
    print("i value is now more than 5")
    
for x in "welcome":
    print(x)
    
f=["apple","banana","coconut"]
for x in f:
    print(x)

g=(12,23,45,67)
total=0
for x in g:
    total=total+x
    print(x)
    #print("total= ",total)
print("total= ",total)

for n in range(5):
    print(n,end='')

for n in range(0,5,1):
    print(n,end='')
    print()
    
for n in range(10,20,1):
    print(n,end='')
    print()
    




