import os

# 获取当前路径
print(os.path.abspath("."))
# 获得父路径
print(os.path.abspath(".."))
file_path = os.path.abspath(".") + "/learn_io.txt"

# 打开文件,以只读的形式打开文件
f = open(file_path, "r")
# 读取文件内容read()读取文件所有内容，如果是大文件，会导致内存爆满
# print(f.read())
# readline() 读取一行，参数limit表示读取多少个字符串，负数表示全部，默认是读取遗憾的全部
# print(f.readline(-5))
print(f.readlines(2))
# 关闭文件流
f.close()
