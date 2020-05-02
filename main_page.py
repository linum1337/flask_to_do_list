from flask import Flask, render_template

app = Flask(__name__)


@app.route('/list')
def list():
    return render_template('main_page.html', title='To_do')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
