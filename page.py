from flask import Flask, redirect, render_template
from AuthForm import LoginForm
from RegForm import RegForm
from TableForm import TableForm
from data import db_session
from data.users import User
from data.Days import DaysInfo
from flask_ngrok import run_with_ngrok
import datetime


app = Flask(__name__)
run_with_ngrok(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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
    session = db_session.create_session()
    form = RegForm()
    password = form.password.data
    password_again = form.password_again.data
    if password == password_again :
        if len(password) > 8 :
            if not password.isdigit() :
                digit_in = False
                for i in range(10) :
                    if str(i) in password :
                        digit_in = True
                if digit_in :
                    if not session.query(User).filter(User.name == form.username.data).first() :
                        if not session.query(User).filter(User.name == form.username.data,
                                                          User.hashed_password == password).first():
                                u = User()
                                u.name = form.username.data
                                u.hashed_password = password
                                session.add(u)
                                session.commit()
                                for i in range(31):
                                    d = DaysInfo()
                                    d.key_id = u.id
                                    session.add(d)
                                session.commit()

                        return redirect('/login')
                    else:
                        return render_template('same_error.html' , title='Регистрация' , form=form)
                else :
                    return render_template('error_reg.html' , title='Регистрация' , form=form)
            else :
                return render_template('error_reg.html' , title='Регистрация' , form=form)
        else :
            return render_template('error_reg.html' , title='Регистрация' , form=form)
    else :
        return render_template('error_reg.html' , title='Регистрация' , form=form)


@app.route('/check_log', methods=['POST'])
def check_log():
    form = LoginForm()
    session = db_session.create_session()
    if session.query(User).filter(User.name == form.username.data, User.hashed_password == form.password.data).first():
        return redirect('/list')
    else:
        return render_template('error_log.html', title='Авторизация' , form=form)


@app.route('/save_info', methods=['POST'])
def save_info():
    session = db_session.create_session()
    form = TableForm()
    if form.validate_on_submit():
        days_info_texts = session.query(DaysInfo).filter(DaysInfo.key_id == User.id).all()
        for i in range(len(form.list_days)):
            days_info_texts[i].text = form.list_days[i].data
        session.commit()
    return redirect('/list')


@app.route('/list', methods=['GET'])
def list():
    form = TableForm()
    session = db_session.create_session()
    days_info_texts = session.query(DaysInfo).filter(DaysInfo.key_id == 1).all()
    for i in range(30):
        form.list_days[i].data = days_info_texts[i].text
    return render_template('main_page.html', title='To_do', form=form)


if __name__ == '__main__':
    db_session.global_init("db/users.sqlite")
    db_session.global_init("db/days.sqlite")
    app.run()
