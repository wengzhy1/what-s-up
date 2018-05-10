# -*- coding: utf-8 -*-

# 计算回数：
# 首先，列出自然数序列：
# 1，2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 序列中的每个数与自身的反转比较，不相等的筛掉：

def is_palindrome(n):
	return str(n) == str(n)[::-1]

print(list(filter(is_palindrome, range(1000,2000))))

def _iter():
	n = 0
	while True:
		n += 1
		yield n

def _judge():
	t = _iter()	# 初始序列
	return filter(is_palindrome, t)


# 打印100以内的回数:
for i in _judge():
	if i < 1000:
		print(i)
	else:
		break