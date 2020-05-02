from flask import Flask, redirect, render_template
from ClassLoginForm import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/list')
def list():
    return render_template('main_page.html', title='To_do')


@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/list')
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
