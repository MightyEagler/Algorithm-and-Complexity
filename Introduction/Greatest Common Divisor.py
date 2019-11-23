# -*- coding: utf-8 -*-
"""
@author: Hongzhi Fu
"""

# Euclid's algorithm to find the greatest common divisor with the complexity O(logn)
def gcd(m, n):
    while n != 0:
        r = m
        m = n
        n = r % n
        gcd(m, n)
    return m
print(gcd(24, 16))
