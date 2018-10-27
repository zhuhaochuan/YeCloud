# 导入:
from sqlalchemy import Column, String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class Userinfo(Base):
    # 表的名字:Userinfo
    __tablename__ = 'userinfo'

    # 表的结构:
    password = Column(String(20))
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

#初始化数据库连接:
engine = create_engine('mysql+pymysql://root:zhc131180176@localhost:3306/user')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)



# 创建session对象:该对象可视为当前数据库的连接
# session = DBSession()
# # 创建新User对象:
# #new_user = Studentlist(student='ppp',id='131180181', name='Bob',age=100)
# # 添加到session:
# #session.add(new_user)
#
# row = session.query(Userinfo).filter(Userinfo.name=='zhcc' , Userinfo.password=='zhc131180176').all()
# print(row)

# print('type:',type(user))
# print('name:',user.name)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()

