# -*- coding: utf-8 -*-

# 假设我们用一组tuple表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：
# 按成绩从高到低排序：

L = [('Bob', 5), ('Boa', 7), ('Adam', 9), ('Bart', 6), ('Lisa', 3)]

def by_name(t):
    return t[0]  #构造

def by_score(t):
    return -t[1]

# print("\nby_name:\n",by_name(L))
# print("\nby_score:\n",by_score(L))
# print("\n原始输入直接排序\n",sorted(L))

L2 = sorted(L, key = by_name)
print("\n按名字排序:\n",L2)

L2 = sorted(L, key = by_score)
print("\n按成绩从高到低排序:\n",L2)
