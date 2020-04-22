from flask import Flask, render_template

app = Flask(__name__)


@app.route('/training')
def training():
    job = 'строитель'
    return render_template('M A R S.html', title='Y E S', job=job)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
