import sqlalchemy
from .db_session import SqlAlchemyBase


class DaysInfo(SqlAlchemyBase):
    __tablename__ = 'DaysInfo'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    text = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    important = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)

