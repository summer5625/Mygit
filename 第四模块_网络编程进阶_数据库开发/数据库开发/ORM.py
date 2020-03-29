# -*- coding: utf-8 -*-
# @Time    : 2019/8/5  9:48
# @Author  : XiaTian
# @File    : ORM.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, UniqueConstraint, ForeignKeyConstraint
from sqlalchemy import Index
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:123456@localhost/db1?charset=utf8', max_overflow=5)
Base = declarative_base()


class Business(Base):
    __tablename__ = 'business'
    id = Column(Integer, primary_key=True, autoincrement=True)
    bname = Column(String(32), nullable=False, index=True)


class Service(Base):
    __tablename__ = 'service'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sname = Column(String(32), nullable=False, index=True)
    ip = Column(String(32), nullable=False)
    port = Column(Integer, nullable=False)
    business_id = Column(Integer, ForeignKey('business.id'))
    __table_args__ = (UniqueConstraint(ip, port, name='uix_ip_port'),
                      Index('ix_id_sname', id, sname))


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


init_db()

Session = sessionmaker(bind=engine)
session = Session()
res = session.query(Business).filter(Business.id > 0, Business.id < 3)
print([(row.id, row.bname) for row in res])
