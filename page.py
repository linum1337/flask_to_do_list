from flask import Flask, redirect, render_template
from AuthForm import LoginForm
from RegForm import RegForm
from data.users import User
from data import db_session
import os, hashlib

app = Flask(__name__)
salt = os.urandom(32)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = StringField('Пароль', validators=[DataRequired()])
    submitL = SubmitField('Авторизоваться')
    butreg = SubmitField('Зарегистрироваться')


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RegForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = StringField('Пароль', validators=[DataRequired()])
    password_again = StringField('Подтвердите пароль', validators=[DataRequired()])
    submitR = SubmitField('Зарегистрироваться')


@app.route('/month_change')
def month_change():
    return render_template('month_change.html', title='Выбор месяца')


@app.route('/registration', methods=['GET'])
def registration():
    form = RegForm()
    return render_template('registration.html', title='Регистрация', form=form)


@app.route('/')
@app.route('/login', methods=['GET'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/check_reg', methods=['POST'])
def check_reg():
    form = RegForm()
    session = db_session.create_session()
    password = form.password.data
    password_again = form.password_again.data
    if password == password_again:
        if len(password) > 8:
            if not password.isdigit():
                digit_in = False
                for i in range(10):
                    if str(i) in password:
                        digit_in = True
                if digit_in:
                    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128)
                    if not session.query(User).filter(User.name == form.username.data,
                                                      User.hashed_password == key).first():
                        u = User()
                        u.name = form.username.data
                        u.hashed_password = key
                        session.add(u)
                        session.commit()
                    return redirect('/login')
                else:
                    return render_template('error_reg.html', title='Регистрация', form=form)
            else:
                return render_template('error_reg.html', title='Регистрация', form=form)
        else:
            return render_template('error_reg.html', title='Регистрация', form=form)
    else:
        return render_template('error_reg.html', title='Регистрация', form=form)


@app.route('/check_log', methods=['POST'])
def check_log():
    form = LoginForm()
    session = db_session.create_session()
    key = hashlib.pbkdf2_hmac('sha256', form.password.data.encode('utf-8'), salt, 100000, dklen=128)
    if session.query(User).filter(User.name == form.username.data, User.hashed_password == key).first():
        return redirect('/month_change')
    else:
        return render_template('error_log.html', title='Авторизация', form=form)


@app.route('/list')
def list():
    return render_template('main_page.html', title='To_do')


if __name__ == '__main__':
    db_session.global_init("db/users.sqlite")
    app.run(port=8080, host='127.0.0.1')
