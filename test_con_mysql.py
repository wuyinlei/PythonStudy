import MySQLdb

# 获取连接
conn = MySQLdb.connect(
    host="127.0.0.1", #主机地址
    user='root', #用户名
    passwd='root', #用户密码
    db='exam',#数据库名字
    port=3306,#端口号
    charset='utf8'#字节码
)  # 获取数据
cursor = conn.cursor()
cursor.execute('SELECT * from user WHERE id = 10')
rest = cursor.fetchone()
# 打印数据
print(rest)

# 关闭连接
conn.close()
