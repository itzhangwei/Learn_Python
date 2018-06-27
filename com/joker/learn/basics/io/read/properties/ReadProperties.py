import configparser
# 使用ConfigParser来读取配置文件

import os

print("获得当前工作目录：" + os.path.abspath('.'))
print("获得当前工作目录的父目录：%s" % os.path.abspath(".."))
print("获得当前工作目录：%s" % os.path.abspath(os.curdir))

# 获取当前文件执行的路径
project_path = os.path.dirname(os.path.abspath(__file__))
print(project_path)

# 获取配置文件对象
config = configparser.ConfigParser()

# 读取配置文件,以 utf8编码打开读取配置文件，默认是gbk，和文件编码不一致会导致读取失败
config.read("E:\\PyCharm_WorkSpace\\learn\\resource\\db.ini", "utf-8")

# 获取mysql节点下的username
username = config.get("mysql", 'username')
print(username)

# 获取配置文件下mysql节点下数据库配置信息
password = config.get("mysql", "password")
print("password = %s" % password)

# 获去配置文件中的节点对象,
mysql_sections = config.items("mysql")
for key in mysql_sections:
    for name in key:
        print(name)
    print(key)

# 项配置文件中写入数据,

# 先判断是否有此节点，如果没有就删除 has_section返回是否有此节点
hasFlag = config.has_section("myWrite")

# not 表示非
if not hasFlag:
    # 添加一个新的节点
    config.add_section("myWrite")
    config.set("myWrite", "myName", "joker")

    # 向节点中写入配置
    with open("E:\\PyCharm_WorkSpace\\learn\\resource\\db.ini", "w") as fw:
        config.write(fw)

else:
    print("myWrite此节点已存在！")
