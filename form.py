from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = StringField('Пароль', validators=[DataRequired()])
    password_again = StringField('Подтвердите пароль', validators=[DataRequired()])
    submitR = SubmitField('Зарегистрироваться')
    submitL = SubmitField('Авторизоваться')
