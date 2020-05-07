from flask import Flask, redirect, render_template
from data import db_session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/list')
def list():
    return render_template('main_page.html', title='To_do')


@app.route('/month_change')
def change():
    return render_template('month_change.html', title='To_do')


if __name__ == '__main__':
    db_session.global_init("db/users.sqlite")
    app.run(port=8080, host='127.0.0.1')
