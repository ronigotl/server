from flask import Flask, redirect, url_for, render_template, request, session, jsonify
import datetime

app = Flask(__name__)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(minutes=20)


# root of our website
@app.route('/')
def index_func():
    return redirect(url_for('Homepage'))


@app.route('/Homepage')
def Homepage():
    return render_template('Homepage.html')


@app.route('/about')
def about_page():
    return render_template('ContactUs.html')


@app.route('/assignment3_1')
def assignment3_1():
    user_name = 'roni'
    city_names = ('tel aviv', 'hifa', 'beersheva')
    countries_names = ['isreal', 'italy', 'Turkey']
    return render_template('assignment3_1.html',
                           user_name=user_name,
                           city_names=city_names,
                           countries_names=countries_names)


users_dict = {
    "1": {"name": "roni", "email": "roni@gmail.com", "user_name": "ronigotl"},
    "2": {"name": "mor", "email": "mor@gmail.com", "user_name": "morgotl"},
    "3": {"name": "gal", "email": "gal@gmail.com", "user_name": "galgotl"},
    "4": {"name": "ran", "email": "ran@gmail.com", "user_name": "rangotl"},
    "5": {"name": "alon", "email": "alon@gmail.com", "user_name": "alongotl"}
}
user_dict = {
    'roni': '1234',
    'mor': '5678',
    'gal': '1122',
    'ran': '3344',
    'alon': '0000',
}


@app.route('/assignment3_2', methods=['GET', 'POST'])
def assignment3_2():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in user_dict:
            pas_in_dict = user_dict[username]
            if pas_in_dict == password:
                session['username'] = username
                session['logedin'] = True
                return render_template('assignment3_2.html',
                                       message='Success',
                                       username=username)
            else:
                return render_template('assignment3_2.html',
                                       message='Wrong password!')
        else:
            return render_template('assignment3_2.html',
                                   message='Please sign in!')

    if 'name' in request.args:
        name = request.args["name"]
        if name == '':
            return render_template('assignment3_2.html', users=users_dict)
        choose = None
        for user_name in users_dict.values():
            if user_name['name'] == name:
                choose = user_name
                break
        if choose:
            return render_template('assignment3_2.html',
                                   name=choose['name'],
                                   email=choose['email'],
                                   user_name=choose['user_name'])
        else:
            return render_template('assignment3_2.html',
                                   message2='No user found')
    return render_template('assignment3_2.html',
                           users=users_dict)


@app.route('/log_out')
def logout_func():
    session['logedin'] = False
    session.clear()
    return redirect(url_for('assignment3_2'))


@app.route('/session')
def session_func():
    # print(session['CHECK'])
    return jsonify(dict(session))


# --------4-------------#
from pages.assignment_4.assignment_4 import assignment_4

app.register_blueprint(assignment_4)

if __name__ == '__main__':
    app.run(debug=True)
