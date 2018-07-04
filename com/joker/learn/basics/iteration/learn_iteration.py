# Python的迭代方式
# 迭代字符串列表
from typing import Iterable

import os

l = list("abcd")
print(l)
for key in l:
    print(key)

# 迭代字典
print("迭代字典".center(100, "="))
dic = {"name": "joker", "age": "23", "sex": "男", "appearance": "handsom"}

# 默认迭代字典的key集合,和下面相等,字典是key是按照hash算法来的，会有输出顺序不同意的情况
print("迭代字典的key集合".center(50, "*"))
for d in dic:
    print(d)

for key in dic.keys():
    print(key)

# 迭代字典的value集合
print("迭代字典的value集合".center(50, "*"))
for v in dic.values():
    print("迭代字典的value集合：" + str(v))

# 迭代字典的key-vaule集合
print("迭代字典的key-vaule集合".center(50, "*"))
for k, v in dic.items():
    print(k + ":" + v)

# 迭代字典的元祖列表
print("迭代字典的元祖列表".center(100, "="))
# 元祖中有多少个数据就可以用多少个变量来代替里面的值，如果只写一个就是列表中的元组，参数只能等于元组中的个数，或者是1
for x, y, z in [(1, 1, "a"), (2, 4, "b"), (3, 9, "c")]:
    print(x, y, z)

for it in [(1, 1, "a"), (2, 4, "b"), (3, 9, "c")]:
    print(it)

# 带有索引下表的迭代,enumerate：将list列表变成 索引-元素对的形式
print("带有索引下表的迭代".center(100, "="))
for i, v in enumerate(["A", "B", "C"]):
    print(i, v)

# v是列表中的元祖对象
for i, v in enumerate([(1, 1, "a"), (2, 4, "b"), (3, 9, "c")]):
    print(i, v)

# dic默认还是迭代字典的key
for i, v in enumerate(dic):
    print(i, v)

# 判断是否是迭代对象
print(isinstance("abc", Iterable))
print(isinstance(123, Iterable))

# 列表生成，结果：[1, 2, 3, 4, 5, 6, 7, 8, 9]
print("列表生成".center(100, "="))
print(list(range(1, 10)))

# 使用循环,结果：['0+1', '1+2', '2+3', '3+4', '4+5', '5+6', '6+7', '7+8', '8+9', '9+10']
print(list(str(i) + "+" + str(i + 1) for i in range(0, 10)))

# 使用双重循环，结果：['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
print([m + n for m in "ABC" for n in "XYZ"])

# os.listdir获取当前目录下的文件和文件夹
print([d for d in os.listdir(".")])

# 循环字典生成列表
print([k + "=" + v for k, v in dic.items()])

# 循环生成列表，把列表中的字符串全部转换为小写
l = ["I", "AM", "VERY", "HANDSOME"]
print([k.lower() for k in l])

# 生成字符串列表
L1 = ['Hello', 'World', 18, 'Apple', None]
L1 = list(k.lower() for k in L1 if isinstance(k, str))
print(L1)

# 生成器 generator：按照算法推算列表元素，在需要的时候计算出列表元素，并不是初始化就算出所有列表元素。
print("generator生成器：".center(100, "="))
g = (x * x for x in range(10))
print(g)
# 调用next方法计算下一个元素值,到最后一个元素的时候会出现StopIteration错误
print(g.__next__())
print(next(g))
# 使用循环遍历生成器
for res in g:
    print(res)
