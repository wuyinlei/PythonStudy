from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

engine = create_engine('mysql://root:root@localhost:3306/python_db')
Base = declarative_base()

Session = sessionmaker(bind=engine)


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


class OrmTest(object):
    def __init__(self):
        self.session = Session()

    def add_one(self):
        # '''新增一条记录'''
        new_obj = News(
            title='title',
            content='content',
            types='2',
        )

        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    def get_one(self):
        '''查询一条数据'''
        return self.session.query(News).get(1)

    def get_more(self):
        '''查询多条数据'''
        return self.session.query(News).filter_by(is_valid=True)

    def update_data(self, pk):
        '''修改数据'''
        new_obj = self.session.query(News).get(pk)
        if new_obj:
            new_obj.is_valid = 0
            self.session.add(new_obj)
            self.session.commit()
            return True
        return False

    # 集合更改
    def update_list_data(self):
        data_list = self.session.query(News).filter_by(is_valid=True)
        for item in data_list:
            item.is_valid = 0
            self.session.add(item)

        self.session.commit()

    # 删除数据
    def delete_data(self):
        '''删除数据'''
        # 获取要删除的数据
        new_obj = self.session.query(News).get(1)
        self.session.delete(new_obj)
        self.session.commit()  # 修改新增删除都需要加上这个commit()


def main():
    obj = OrmTest()
    rest = obj.updata_data(1)
    print(rest)


if __name__ == '__main__':
    main()
