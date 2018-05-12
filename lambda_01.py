# -*- coding: utf-8 -*-

def is_odd(n):
    return n % 2

L = list(filter(is_odd, range(1, 20)))
print(L)

L = list(filter(lambda x: x % 2, range(1, 20)))
print(L)

#匿名函数作为返回值返回 ??
def build(x):
    return lambda: x * x

print(list(filter(build, range(1, 20))))
