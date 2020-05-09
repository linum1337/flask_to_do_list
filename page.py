from flask import Flask, redirect, render_template
from AuthForm import LoginForm
from RegForm import RegForm
from TableForm import TableForm
from data import db_session
from data.users import User
from data.Days import DaysInfo
import datetime
import calendar


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
user_name = ''


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
    today = datetime.datetime.today()
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
                                for i in range(35):
                                    d = DaysInfo()
                                    d.data = (today + datetime.timedelta(days=i)).strftime("%d/%m/%y")
                                    d.user_name = u.name
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
    global user_name
    user_name = form.username.data
    session = db_session.create_session()
    if session.query(User).filter(User.name == form.username.data, User.hashed_password == form.password.data).first():
        today = datetime.datetime.today()
        days_info = session.query(DaysInfo).filter(user_name == DaysInfo.user_name).all()
        old_dates_dict = {}
        old_dates_list = []
        if days_info[0].data != today.date() :
            for i in range(35):
                if days_info[i].data != (today + datetime.timedelta(days=i)).strftime("%d/%m/%y"):
                    old_dates_dict[days_info[i].data] = days_info[i].text
                    old_dates_list.append(days_info[i].data)
                    days_info[i].text = ''
                    days_info[i].data = (today + datetime.timedelta(days=i)).strftime("%d/%m/%y")
            for i in old_dates_list:
                for j in range(35):
                    if days_info[j].data == i:
                        days_info[j].text = old_dates_dict[i]
            session.commit()
        return redirect('/list')
    else:
        return render_template('error_log.html', title='Авторизация' , form=form)


@app.route('/save_info', methods=['POST'])
def save_info():
    global user_name
    session = db_session.create_session()
    form = TableForm()
    if form.validate_on_submit():
        if session.query(DaysInfo).filter(user_name == DaysInfo.user_name).all():
            days_info = session.query(DaysInfo).filter(user_name == DaysInfo.user_name).all()
            for i in range(len(form.list_days)):
                days_info[i].text = form.list_days[i].data
            session.commit()
    return redirect('/list')


@app.route('/list', methods=['GET'])
def list():
    list_weekdays = {"Mon" : 'Понедельник' , "Tue" : 'Вторник' , "Wed" : 'Среда' , "Thu" : 'Четверг' ,
                     "Fri" : 'Пятница' , "Sat" : 'Суббота' , "Sun" : 'Воскресенье'}
    global user_name
    form = TableForm()
    session = db_session.create_session()
    days_info = session.query(DaysInfo).filter(DaysInfo.user_name == user_name).all()
    for i in range(35):
        form.list_days[i].data = days_info[i].text
        data = list_weekdays[calendar.day_abbr[datetime.datetime.strptime(days_info[i].data,
                                                                          "%d/%m/%y").date().weekday()]]
        form.list_dates[i].data = [days_info[i].data, data]
    return render_template('main_page.html', title='To_do', form=form)


if __name__ == '__main__':
    db_session.global_init("db/users.sqlite")
    db_session.global_init("db/days.sqlite")
    app.run(port=8080 , host='127.0.0.1', debug=True)
