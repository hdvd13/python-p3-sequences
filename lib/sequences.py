#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fib = [0, 1]
        i = 2
        while i < length:
            fib.append(fib[i-1] + fib[i-2])
            i += 1
        
        print(fib)