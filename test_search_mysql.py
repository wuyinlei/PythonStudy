import MySQLdb


# 定义搜索类
class MySqlSearch(object):
    def __init__(self):
        self.conn = MySQLdb.connect(
            host="127.0.0.1",  # 主机地址
            user='root',  # 用户名
            passwd='root',  # 用户密码
            db='exam',  # 数据库名字
            port=3306,  # 端口号
            charset='utf8'  # 字节码
        )
        self.get_conn()

    # 获取连接
    def get_conn(self):

        try:
            pass
        except MySQLdb.Error as e:
            print('Error :%s ' % e)

    # 关闭连接
    def close_conn(self):
        try:
            if self.conn:
                # 关闭连接
                self.conn.close()
        except MySQLdb.Error as e:
            print('Error : %s ' % e)

    # 获取单个搜索
    def get_one(self):
        # 准备sql
        sql = 'SELECT * from user'
        # 找到cursor
        cursor = self.conn.cursor()
        # 执行sql
        # print(dir(cursor))
        cursor.execute(sql)
        # 拿到结果
        rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        # 处理数据
        # print(rest)
        # 关闭连接
        cursor.close()
        self.close_conn()
        return rest

    # 获取所有搜索
    def get_more(self):
        sql = 'SELECT * from user'
        # 找到cursor
        cursor = self.conn.cursor()
        # 执行sql
        # print(dir(cursor))
        cursor.execute(sql)
        # 拿到结果
        rest = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall()]
        # 关闭连接
        cursor.close()
        self.close_conn()
        return rest

    # 分页搜索
    def get_page(self, page, page_size):
        offset = (page - 1) * page_size
        sql = 'SELECT * from user LIMIT %s,%s'
        # 找到cursor
        cursor = self.conn.cursor()
        # 执行sql
        # print(dir(cursor))
        cursor.execute(sql, (offset, page_size))
        # 拿到结果
        rest = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall()]
        # 关闭连接
        cursor.close()
        self.close_conn()
        return rest


def main():
    obj = MySqlSearch()
    result = obj.get_page(1, 5)
    for item in result:
        print(item['username'])
        print('------')
        # print(result['username'])


if __name__ == '__main__':
    main()
