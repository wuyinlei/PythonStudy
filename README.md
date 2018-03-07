# Python学习-Python链接MySql数据库

标签（空格分隔）： Python

---

### 第一步:配置环境


#### 配置python环境
* 上网百度一下就可以了啦

#### 配置mysql环境
* mac中打开命令行输入

    ```
    sudo pip3 install mysqlclient（按下enter执行即可(需要先安装过mysql)）
    ```
#### 检测是否安装成功
```
import MySQLdb (按下enter如果不报错就证明成功)
```

### 连接数据库
```
import MySQLdb

# 获取连接
conn = MySQLdb.connect(
    host="127.0.0.1",
    user='root',
    passwd='root',
    db='exam',
    port=3306,
    charset='utf8'
)  # 获取数据
cursor = conn.cursor()
cursor.execute('SELECT * from user WHERE id = 10')
rest = cursor.fetchone()
# 打印数据
print(rest)

# 关闭连接
conn.close()


## 控制台输出的结果
(10, '张三', datetime.date(2014, 7, 10), '1', '北京市')
```

### 搜索简单封装
```
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

```

### 插入修改数据库操作


## sqlalchemy 操作数据库

### sqlalchemy安装
```

```

### sqlalchemy是否安装成功

### 创建表
```
#导入sqlalchemy的引擎
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
#导入sqlalchemy的相关类型
from sqlalchemy import Column, Integer, String, DateTime, Boolean
#第一个root是用户名  第二个root是密码 python_db是数据库名称
engine = create_engine('mysql://root:root@localhost:3306/python_db')
Base = declarative_base()

#创建数据model
class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(2000), nullable=False)
    types = Column(String(10), nullable=False)
    image = Column(String(300), nullable=True)
    author = Column(String(20), nullable=True)
    view_count = Column(Integer)
    create_at = Column(DateTime)
    is_valid = Column(Boolean)

```

### 命令行执行创建News
首先创建`python_db`数据库
然后在`pycharm`的命令行中输入`python3`(我这边是直接切换到了`python3`环境中)
输入以下语句
```
from test_mysql_orm import News

from test_mysql_orm import engine

News.metadata.create_all(engine)

```
输入以上最后一句之后按下`enter` 如果不报错则表示执行成功,这个时候去看下数据库`python_db`中会有一个`News`表

### 通过orm向数据库中新增一条数据
#### 引入包
```
from sqlalchemy.orm import sessionmaker
```
#### 绑定
```
Session = sessionmaker(bind=engine)

```
#### 定义测试类
```
class OrmTest(object):
    def __init__(self):
        self.session = Session()

    def add_one(self):
        # '''新增一条记录'''
        new_obj = News(
            title='title',
            content='content',
            types='types',
        )

        self.session.add(new_obj)
        self.session.commit()
        return new_obj

```
#### 运行代码
```
控制台输出 `1`
```

### 查询数据
```
def get_one(self):
    '''获取一条数据'''
    return self.session.query(News).get(1)

def get_more(self):
    '''获取多条数据'''
    return self.session.query(News).filter_by(is_valid=1)
```

### 通过orm修改和删除数据
#### 修改数据
```
def update_data(self):
    '''修改数据'''
    obj = self.session.query(News).get(38)
    obj.id_valid = 0
    self.session.add(obj)
    self.session.commit()
    return obj
```
#### 删除数据
```
def delete_data(self):
    '''删除数据'''
    data = self.session.query(News).get(39)
    self.session.delete(data)
    # 修改新增删除都需要加上这个commit()
    self.session.commit()
```