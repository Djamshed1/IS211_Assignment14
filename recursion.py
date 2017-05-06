#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 14 fibonnaci gcd and compareTo assignment"""

def fibonnaci(n):
    """Implement the fibonnaci Sequence"""
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonnaci(n-1) + fibonnaci(n-2)

def gcd(a, b):
    """Implement Euclid’s GCD Algorithm"""
    while b:
        (a, b) = (b, (a % b))
    return a
    
def compareTo(s1, s2):
    """Compare String"""
    if len(s1) < len(s2):
        return int(-1)
    elif len(s1) == len(s2):
        return int(0)
    elif len(s1) > len(s2):
        return int(1)
