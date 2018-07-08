#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 a test module
"""

__author__ = "Joker"

# 第 1 行和第 2 行是标准注释，第 1 行注释可以让这个 hello.py 文件直接
# 在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8
# 编码；
# 第 4,5,6 行是一个字符串，表示模块的文档注释，任何模块代码的第一个字
# 符串都被视为模块的文档注释；
# 第 8 行使用 __author__ 变量把作者写进去，这样当你公开源代码后别人
# 就可以瞻仰你的大名；
# 以上就是 Python 模块的标准文件模板，当然也可以全部删掉不写，但
# 是，按标准办事肯定没错

import sys


def test():
    """
    测试模块中的方法，简单判断，打印输出一下数据。


    :return: NONE
    """
    # sys.argv用list的形式来存出命令行的参数
    args = sys.argv
    if len(args) == 1:
        print("Hello world !")
    elif len(args) == 2:
        print("Hello %s" % args[0])
    else:
        print("too many arguments!")
    pass


if __name__ == "__main__":
    test()
