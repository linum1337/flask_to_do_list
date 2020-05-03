from flask import Flask, redirect, render_template
from form import Form
from data.users import User
from data import db_session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = Form()
    session = db_session.create_session()
    if form.validate_on_submit():
        password = form.password.data
        password_again = form.password_again.data
        if password == password_again:
            if len(password) > 8 :
                if not password.isdigit():
                    digit_in = False
                    for i in range(10):
                        if str(i) in password:
                            digit_in = True
                    if digit_in:
                        u = User()
                        u.name = form.username.data
                        u.hashed_password = form.password.data
                        session.add(u)
                        session.commit()
                        return redirect('/login')
                    else :
                        return render_template('error_reg.html' , title='Регистрация' , form=form)
                else :
                    return render_template('error_reg.html' , title='Регистрация' , form=form)
            else :
                return render_template('error_reg.html' , title='Регистрация' , form=form)
        else:
            return render_template('error_reg.html' , title='Регистрация' , form=form)
    return render_template('registration.html', title='Регистрация', form=form)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Form()
    session = db_session.create_session()
    if form.validate_on_submit():
        print('ok')
        if session.query(User).filter(User.name == form.username.data, User.hashed_password == form.password.data):
            print('ok')
        redirect('/ссылка')
        return render_template('error_log.html', title='Авторизация' , form=form)
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    db_session.global_init("db/users.sqlite")
    app.run(port=8080, host='127.0.0.1')
