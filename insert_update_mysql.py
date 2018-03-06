import MySQLdb


# 定义搜索类
class MySqlInsert(object):
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

    # 插入单个语句
    def insert_one(self):
        try:
            # 准备sql
            sql = ("INSERT INTO  `user`(`username`,`birthday`,`sex`,`address`) VALUES""(%s, %s, %s, %s);")
            # 找到cursor
            cursor = self.conn.cursor()
            # 执行sql
            cursor.execute(sql, ('砖石王老歪', '2029-12-13', 1, '河南省郑州市'))
            # 提交数据到数据库
            self.conn.commit()
            # 关闭连接
            cursor.close()
            self.close_conn()
        except:
            print('error')
            #出现错误之后需要回滚
            self.conn.rollback()


def main():
    obj = MySqlInsert()
    obj.insert_one()


if __name__ == '__main__':
    main()
