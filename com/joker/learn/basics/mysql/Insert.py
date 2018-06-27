import uuid
import pymysql
# 导入连接数据库工具类
from com.joker.learn.basics.mysql.ConnectUtils import ConnectUtils

# 使用工具类，获取数据库连接
# connect = ConnectUtils.get_connect()
# connect.autocommit(True)

# 获取操作数据库的游标对象
cursor = ConnectUtils.get_cursor()

# 开启事物自动提交
cursor.connection.autocommit(True)
# 查询一下数据库
sql = "SELECT * FROM T_USER"
affect_count = cursor.execute(sql)
print(affect_count)

# 获取结果集
fetchall = cursor.fetchall()
print(fetchall)

# 插入数据
user = {"id": str(uuid.uuid1()).replace("-", ""), "name": "张三", "age": "23", "sex": "1"}
for key in user:
    print(key)
    print(user.get(key))

# \是在pycharm中换行
insert_sql = "INSERT INTO T_USER (ID,NAME,AGE,SEX) VALUES (%s,%s,%s,%s ) "

print(insert_sql)
print(list(user.values()))
print(user.values())

# 插入数据 user.values() 获得的数据是这样的：dict_values(['3a5d1ed0746e11e8b2d350465dea9c6e', '张三', '23', '1'])
# 可使用转换为list来消除前面的dict_values
# cursor.execute(insert_sql, list(user.values()))

# 获取影响行数
row_count = cursor.rowcount
print("影响行数:" + str(row_count))

# 提交事物 ,或则在上面开启自动提交事物
# cursor.connection.commit()

# 从另一个数据读取数据，批量插入到本地的数据库里面
# 创建一个新的数据库连接，获取到游标对象操作数据
db2_info = {
    "host": "47.94.197.87",
    "user": "jsyfstore",
    "password": "myLoveJSYF.com",
    "port": 3501,
    "database": "store_v1",
    "charset": "utf8"
}
db2_arr = [
    "47.94.197.87",
    "jsyfstore",
    "myLoveJSYF.com",
    "store_v1",
    3501,
    "utf8"
]
# def Connect(*args, **kwargs): 三种方法后去连接对象：
# 1. 方法中指定对应参数例如：
#  pymysql.connect(host=url, user=username, passwd=password, port=port,db=database, charset=charset)
# 2.采用对应的json对象格式来指定键值对，但是在传递参数的时候需要带有两个**
# 例如：connect2 = pymysql.connect(**db2_info)

# 3，采用数组，直接把对应的数值写进去，但是对应的需要确定顺序，在源码中可以看到顺序：参数需要带一个*来确定使用哪种参数，
# 例如：connect2 = pymysql.connect(*db2_arr)
connect2 = pymysql.connect(**db2_info)
print(connect2)

# 获取游标对象 cursor()会以数组接口处理查询结果集
# 游标操作数据的时候加入这个，以键值对的形式来处理结果集cursor(pymysql.cursors.DictCursor)
cursor2 = connect2.cursor(pymysql.cursors.DictCursor)

# 从数据源二中查询十条数据
cursor2.execute("SELECT ID AS id,NICK_NAME AS nick_name FROM S_CUSTOMER LIMIT 10")
# 获取所有结果
customer_list = cursor2.fetchall()
age = 20
for row in customer_list:
    age = age + 1
    row['age'] = age
    row['sex'] = '1'
print("查询出来的数组："+customer_list.__str__())
print("集合数组长度:"+ len(customer_list).__str__())

# 批量添加
batch_insert_sql = 'INSERT INTO t_user VALUES '

# 定义数组，接受每一个占位符的数值
value_arr = []

# 循环组织占位符,和value_arr
for row in customer_list:
    # dict将row转换成键值对对象
    row = dict(row)
    # extend 将一个数组的值继续想数组
    value_arr.extend(list(row.values()))

    batch_insert_sql = batch_insert_sql + "( "

    for key in row.keys():
        if key == 'sex':
            batch_insert_sql = batch_insert_sql + "%s"
        else:
            batch_insert_sql = batch_insert_sql + "%s,"

    if customer_list.index(row) == len(customer_list) - 1:
        batch_insert_sql = batch_insert_sql + ") "
    else:
        batch_insert_sql = batch_insert_sql + " ),"

# 打印批量插入sql
print(batch_insert_sql)
print(value_arr)

# 批量插入到本地数据库中
cursor.execute(batch_insert_sql,value_arr)

# 获取影响行数
print("影响行数："+str(cursor.rowcount))