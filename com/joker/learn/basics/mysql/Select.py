from com.joker.learn.basics.mysql.ConnectUtils import ConnectUtils
import pymysql

# 连接mysql，查询数据表，对数据进行查询操作

# 获取mysql连接,使用工具类获取数据库连接
connect = ConnectUtils.get_connect()

# 开启事物自动提交
connect.autocommit(True)

# 获取游标对象，并且设置有表处理结果集以键值对的方式
cursor = connect.cursor(pymysql.cursors.DictCursor)

sql = "SELECT * FROM t_user"

# 执行查询
cursor.execute(sql)

# 获取结果集
results = cursor.fetchall()

print(results)

# sort
# 采用Python来对数组对象进行排序,按照你年龄来排序,倒叙
results = list(results)
results.sort(key=lambda k: (k.get('AGE')), reverse=True)
print(results)
# 先按照年龄，在按照ID双重排序
results.sort(key=lambda k: (k.get("AGE"), k.get("ID")), reverse=True)
print("按照年龄和ID双重排序：" + str(results))

# filter
# 采用python筛选 filter筛选方法，参数1是回调函数，返回True或者False,参数二是需要筛选的对象。
filter_list = list(filter(lambda customer: customer.get("AGE") > 25, results))
print("年龄大于25岁的：" + str(filter_list))
print(results)

# 筛选年龄大于25岁，并且是女的
filter_list2 = list(filter(lambda cus: cus.get("AGE") < 25 and cus.get("SEX") == 1, results))
print("年龄大于25，并且是女的：" + str(filter_list2))


# map 第一个参数函数对象，第二个参数Iterator序列，map对iterator序列中每一个元素进行操作

# 提取每一个用户的姓名,年龄出来 ,使用list函数转换
def get_name(cus):
    # 创建空字典方式
    # user = {}
    user = dict()
    user["Name"] = cus.get("NAME")
    user["age"] = cus.get("AGE")
    return user


# 调用上面的方法，获取用户名称，和年龄
map_cus = list(map(get_name, results))
print(map_cus)

# 采用lambda写法,获取用户名
# 使用lambda函数应该注意的几点：
#
# lambda定义的是单行函数，如果需要复杂的函数，应该定义普通函数
# lambda参数列表可以包含多个参数，如 lambda x, y: x + y
# lambda中的表达式不能含有命令，而且只限一条表达式
map_cus2 = list(map(lambda cus: {"NAME": cus.get("NAME"), "age": cus.get("AGE")}, results))
print(map_cus2)


# 在python中有时候能看到定义一个def函数，函数内容部分填写为pass。
#
# 这里的pass主要作用就是占据位置，让代码整体完整。如果定义一个函数里面为空，
#
# 那么就会报错，当你还没想清楚函数内部内容，就可以用pass来进行填坑。

# Python 参数定义** 表示你可以传递多个参数，这些参数被封装成字典，
# *表示可以传递多个参数，这些参数被封装成tuple类型 见博客：https://blog.csdn.net/weixin_39769379/article/details/78373357
def _add_where(select_sql, sql_args, **query):
    # sql_args = list(sql_args)
    # 对查询条件参数进行非空判断
    # args 是None FALSE ,空列表[]，空字典{},空元祖(),0都会被转为FALSE
    if not query:
        return
    name = query.get("name")
    if name:
        select_sql = select_sql + " AND user.NAME = %s "
        sql_args.append(name)

    user_id = query.get("userId")
    if user_id:
        select_sql = select_sql + " AND user.ID = %s "
        sql_args.append(user_id)

    # 关键字模糊查询
    query_key = query.get("queryKey")
    if query_key:
        # %是python格式化的符号，这里模糊查找需要写双重%%
        select_sql = select_sql + " AND user.NAME LIKE CONCAT('%%',%s,'%%') "
        sql_args.append(query_key)

    # 由于python对于字符串和数值类型采用的值传递，所以需要返回sql语句
    return select_sql


def _add_limit(select_sql, page, rows, sql_args):
    # 判断一个数是否是整数
    if not isinstance(page, int) or not isinstance(rows, int) or rows <= 0 or page < 1:
        return select_sql
    else:
        select_sql = select_sql + " LIMIT %s ,%s "
        sql_args.append((page - 1) * rows)
        sql_args.append(rows)

    # 由于python对于字符串和数值类型采用的值传递，所以需要返回sql语句
    # 1.Python不允许程序员选择采用传值还是传 引用。Python参数传递采用的肯定是“传对象引用”的方式。实际上，这种方式相当于传值和传引用的一种综合。如果函数收到的是一个可变对象（比如字典 或者列表）的引用，就能修改对象的原始值——相当于通过“传引用”来传递对象。如果函数收到的是一个不可变对象（比如数字、字符或者元组）的引用，就不能 直接修改原始对象——相当于通过“传值”来传递对象。
    # 2.当人们复制列表或字典时，就复制了对象列表的引用同，如果改变引用的值，则修改了原始的参数。
    # 3.为了简化内存管理，Python通过引用计数 机制实现自动垃圾回收功能，Python中的每个对象都有一个引用计数，用来计数该对象在不同场所分别被引用了多少次。每当引用一次Python对象，相 应的引用计数就增1，每当消毁一次Python对象，则相应的引用就减1，只有当引用计数为零时，才真正从内存中删除Python对象。

    return select_sql


# 关于方法变量前导和后导下滑线说明，博客：https://blog.csdn.net/youngbit007/article/details/61616241


# 调用动态sql查询数据
select_sql = "SELECT ID AS id ,NAME AS name ,AGE AS age ,SEX as sex FROM t_user AS user WHERE 1=1 "
query = {"name": "", "page": 1, "rows": 10, "queryKey": "灜沣"}
select_args = list()
select_sql = _add_where(select_sql, select_args, **query)
select_sql = _add_limit(select_sql, 1, 10, select_args)

print("sql语句：" + str(select_sql))
print("sql参数：" + str(select_args))

# 执行sql语句
cursor.execute(select_sql, select_args)
user_list = cursor.fetchall()

print(user_list)
print("查询数量："+str(cursor.rowcount))
# 关闭数据源
ConnectUtils.connect_close(cursor)
