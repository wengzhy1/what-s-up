# -*- coding: utf-8 -*-

from functools import reduce

def str2float(s):
	def _init_(t):
		DIGITS = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6':6}
		return DIGITS[t]
	a,b = s.split('.')
	b = b[::-1]
	return reduce(lambda x, y: 10 * x + y, map(_init_, a)) + 0.1 * reduce(lambda x, y: 0.1 * x + y, map(_init_, b))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')