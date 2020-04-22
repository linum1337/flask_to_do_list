from flask import Flask, render_template

app = Flask(__name__)


@app.route('/list')
def list():
    return render_template('main_page.html', title='To_do')


@app.route('/monday')
def monday():
    return render_template('monday.html', title='monday')


@app.route('/tuesday')
def tuesday():
    return render_template('tuesday.html', title='tuesday')


@app.route('/wednesday')
def wednesday():
    return render_template('wednesday.html', title='wednesday')


@app.route('/thursday')
def thursday():
    return render_template('thursday.html', title='thursday')


@app.route('/friday')
def friday():
    return render_template('friday.html', title='friday')


@app.route('/saturday')
def saturday():
    return render_template('saturday.html', title='satuday')


@app.route('/sunday')
def sunday():
    return render_template('sunday.html', title='sunday')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
