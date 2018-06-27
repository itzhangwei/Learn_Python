import mysql.connector
import traceback
import uuid
# 安装pyMysql： python -m pip install pymysql
try:
    # 创建连接 ,没有指定连接的数据库
    connection = mysql.connector.connect(host='localhost',
                                         port='3306',
                                         user='root',
                                         password='zhangwei')

    print(connection)
    # 使用cursor获取操作游标
    cursor = connection.cursor()
    # 执行sql语句，创建表
    cursor.execute("DROP DATABASE IF EXISTS Learn_Python");
    cursor.execute("CREATE DATABASE Learn_Python CHARACTER SET utf8 COLLATE utf8_bin")
    print("python-------->  创建Learn_Python数据库成功!")
    # 选中创建的数据库
    cursor.execute("USE %s" % 'Learn_Python')
    print("python-------->  选择使用Learn_Python数据库成功!")
    # 创建数据表
    TABLE_NAME = "T_USER"

    # 如果表存在就删除表
    cursor.execute(" DROP TABLE IF EXISTS %s " % TABLE_NAME)

    # 创建表sql语句拼接
    createTableSql = "CREATE TABLE %s(ID VARCHAR(32) PRIMARY key COMMENT '主键ID', "
    createTableSql += " NAME VARCHAR(32) NOT NULL COMMENT '姓名' , "
    createTableSql += " AGE INT(2) NOT NULL COMMENT '年龄',"
    createTableSql += " SEX CHAR(1) DEFAULT '1' COMMENT '1：男，0：女') "
    cursor.execute(createTableSql % TABLE_NAME)
    print("python-------->  创建T_USER表创建成功!")

    # 插入数据
    id = str(uuid.uuid1())
    joker = [id.replace("-", ""), 'joker', 24, '1']
    print(joker)
    cursor.execute("INSERT INTO T_USER VALUES (%s,%s,%s,%s) ", joker)
    print("python-------->  插入数据到T_USER表中成功!")

    # 事务提交,连接对象提交事物的
    connection.commit()
    print("python-------->  事务提交!")
except:
    # 异常打印
    traceback.print_exception()
    # 事物回滚
    connection.rollback()
    print("python-------->  异常，事物回滚!")
finally:
    # 关闭资源
    cursor.close()
    connection.close()
    print("python-------->  资源关闭!")
