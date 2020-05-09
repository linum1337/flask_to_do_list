import sqlalchemy
from .db_session import SqlAlchemyBase


class DaysInfo(SqlAlchemyBase):
    __tablename__ = 'DaysInfo'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    text = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user_name = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    data = sqlalchemy.Column(sqlalchemy.String, nullable=True)
