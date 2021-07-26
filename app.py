from flask import Flask, render_template, request, flash
from functions import findGitData

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        login = request.form['login']
        if login.strip() == '':
            flash('Please, enter login!', 'danger')
        else:
            return render_template('index.html', data=findGitData(login))
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
