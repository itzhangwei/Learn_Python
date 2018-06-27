import pymysql
import configparser
import os


# 读取配置文件方法
class ConnectUtils:

    # @staticmethod 是静态方法注解，@classmethond是普通类方法
    @staticmethod
    def get_connect():
        # 获得当前的目录
        db_path = os.path.abspath(".") + "\database.ini"

        # 获取配置文件读取对象
        config = configparser.ConfigParser()

        # 读取配置文件，以utf8的编码格式读取数据库配置文件
        config.read(db_path, "utf-8")

        # 获取mysql节点下信息
        url = config.get("mysql", "url")
        port = config.getint("mysql", "port")
        username = config.get("mysql", "username")
        password = config.get("mysql", "password")
        database = config.get("mysql", "database")
        charset = config.get("mysql", "charset")

        # 连接mysql

        # host(str): MySQL服务器地址
        # port(int): MySQL服务器端口号
        # user(str): 用户名
        # passwd(str): 密码
        # db(str): 数据库名称
        # charset(str): 连接编码
        try:
            connect = pymysql.connect(host=url, user=username, passwd=password, port=port,
                                      db=database, charset=charset)

            return connect
        except:
            # 连接数据库异常，返回一个空的对象
            return None

        #
        # connection对象支持的方法
        # cursor()
        # 使用该连接创建并返回游标
        # commit()
        # 提交当前事务
        # rollback()
        # 回滚当前事务
        # close()
        # 关闭连接
        #
        # cursor对象支持的方法
        # execute(op)
        # 执行一个数据库的查询命令
        # fetchone()
        # 取得结果集的下一行
        # fetchmany(size)
        # 获取结果集的下几行
        # fetchall()
        # 获取结果集中的所有行
        # rowcount()
        # 返回数据条数或影响行数
        # close()
        # 关闭游标对象

    # 获得游标对象，操作数据库对象
    @staticmethod
    def get_cursor():
        connect = ConnectUtils.get_connect()
        # 空指针判断
        if connect:
            return connect.cursor()
        else:
            return None;

    # 关闭游标对象
    @staticmethod
    def connect_close(cursor):
        if cursor:
            cursor.close()
