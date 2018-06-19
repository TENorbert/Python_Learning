#!/usr/bin python

import time as dt

def fact(num):
    """ Simple Recursion version """
    try:
        if num <= 1:
            return 1
        else:
            return num*fact(num-1)
    except Exception as e:
        print(e, type(e))


def dp_fact(num):
    """Dynamic Programming Version"""
    if num < 0:
        print("For the Love of God, Enter a positive Number!")
    try:
        f = [None]*(num + 1)
        f[0] = 1
        f[1] = 1
    	#Subprograms
        for i in range(2,num+1):
            f[i] = i*f[i-1]
        
        return f[num]
    except Exception as e:
        print(e, type(e))


# Performance Testing
N = int(input("Enter Number to Compute Factorial "))
srt = dt.time()
fact(N)
stp = dt.time()
elapse = stp-srt
print("Factorial of {0} is = {1}".format(N, fact(N)))
print("Factorial time = %s seconds " %(elapse))

srt = dt.time()
dp_fact(N)
stp = dt.time()
elapse = stp-srt
print("DP Factorial of {0} is = {1}".format(N, dp_fact(N)))
print("DP Fcatorial time = %s seconds " %(elapse))
