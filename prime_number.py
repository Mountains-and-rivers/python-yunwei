#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# def prime(n):
#         m = 0
#         for i in range(2, n):
#             j = 2
#             for j in range(2, int(i**0.5)+1):
#                 if i % j == 0:
#                     break
#             else:
#                 m += 1
#         return m

# print(prime(10))

def su(a,b):
    for i in range(a,b):
        n = False #默认不是素数，如果是素数，跳出循环
        for j in range(2,int(i**0.5)):
            if i%j == 0:
                n = True
                break

        if n == False:
            print(i,end=" ")

su(100,200)