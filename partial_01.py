#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

int2 = functools.partial(int, base=2)

print("int2('1000000') =", int2('1000000'))
print("int2('1010101') =", int2('1010101'))
print("int2('1000000', base=2) =", int2('1000000', base=10))

max2 = functools.partial(max, 10)

print("max2(5, 6, 7) =", max2(5, 6, 7))
print("max2(15, 16, 17) =", max2(15, 16, 17))
