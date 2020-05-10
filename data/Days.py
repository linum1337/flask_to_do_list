# import sqlalchemy
# from .db_session import SqlAlchemyBase
# from data.users import User
#
#
# class DaysInfo(SqlAlchemyBase):
#     __tablename__ = 'DaysInfo'
#
#     id = sqlalchemy.Column(sqlalchemy.Integer,
#                            primary_key=True, autoincrement=True)
#     text = sqlalchemy.Column(sqlalchemy.String, nullable=True)
#     user_name = sqlalchemy.Column(sqlalchemy.VARCHAR, sqlalchemy.ForeignKey(User.name))
#     data = sqlalchemy.Column(sqlalchemy.String, nullable=True)

