import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from sqlalchemy import ForeignKey


class User(SqlAlchemyBase):
    __tablename__ = 'users'
    name = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name_days_info = orm.relationship("DaysInfo", uselist=False, back_populates="name_user")


class DaysInfo(SqlAlchemyBase) :
    __tablename__ = 'DaysInfo'

    id = sqlalchemy.Column(sqlalchemy.Integer , primary_key=True)
    text = sqlalchemy.Column(sqlalchemy.String , nullable=True)
    data = sqlalchemy.Column(sqlalchemy.String , nullable=True)
    user_name = sqlalchemy.Column(sqlalchemy.String, ForeignKey('users.name'))
    name_user = orm.relationship("User", back_populates="name_days_info")
