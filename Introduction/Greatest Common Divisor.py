# -*- coding: utf-8 -*-
"""
@author: Hongzhi Fu
"""

def gcd(m, n):
    while n != 0:
        r = m
        m = n
        n = r % n
        gcd(m, n)
    return m
print(gcd(24, 16))