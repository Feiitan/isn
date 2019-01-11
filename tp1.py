# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 10:27:10 2019

@author: azhu
"""
def coucou(n) :
    a = 0
    while n !=1  :
        if n % 2 == 0 :
            n = n // 2
        else :
            n = 3 * n + 1
        a = a + 1
    return a

def main() :
    for i in range(0,1000) :
        a = coucou(i)
        print(i, a)
main()
