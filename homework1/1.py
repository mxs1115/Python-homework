#!/usr/bin/python3
# -*- coding: utf-8 -*-

#元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数；

print("0--50之间的偶数有：")
for i in range(51):
    if ( i%2 == 0 ):
        print( i, end=" " )
print()

print("0--50之间的奇数有: ")
for i in range(51):
    if( i%2 != 0 ):
        print( i, end=" " )
print()
    
print("0--50之间的质数有：")
for i in range(51):
    x=2
    while( x < i ):
        if( i%x == 0 ):
            break
        else:
            x=x+1
            continue   
    if( x == i ):
        print( i, end=" " ) 
print()

print("0--50之间能同时被2和3整除的数: ")
for i in range(51):
    if( i%2==0 and i%3==0 ):
        print(i,end=" ")