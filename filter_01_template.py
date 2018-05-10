# -*- coding: utf-8 -*-

def _odd_iter():
	n = 2
	while True:
		n += 1
		yield n

def _not_divisible(n):
	return lambda x: x % n > 0

def primes():
	print(2)
	t = _odd_iter()	# 初始序列
	while True:
		n = next(t)	# 返回序列的第一个数
		yield n
		t = filter(_not_divisible(n), t)	 # 构造新序列

# 打印100以内的素数:
for i in primes():
	if i < 100:
		print(i)
	else:
		break