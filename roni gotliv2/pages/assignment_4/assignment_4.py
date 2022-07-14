import os
import mysql.connector
from flask import Blueprint, render_template, request, redirect, jsonify
import requests
from dotenv import load_dotenv
load_dotenv()




assignment_4 = Blueprint('assignment_4', __name__, static_folder='static', template_folder='templates')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host=os.getenv('DB_HOST'),
                                         user=os.getenv('DB_USER'),
                                         passwd=os.getenv('DB_PASSWORD'),
                                         database=os.getenv('DB_NAME'))
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    #

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


# Routes
@assignment_4.route('/assignment_4')
def main():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('assignment_4.html', users=users_list)


# INSERT #
@assignment_4.route('/insert_user', methods=['POST'])
def insert_user():
    name = request.form['name']
    email = request.form['email']
    user_name = request.form['user_name']
    password = request.form['password']
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    for user in users_list:
        if name == user.name:
            return render_template('assignment_4.html', users=users_list)
    print('f{name} {email} {user_name} {password}')
    query = "INSERT INTO users(name, email,user_name, password) VALUES ('%s', '%s', '%s', '%s')"% (name, email, user_name ,password)
    interact_db(query=query, query_type='commit')
    return render_template('assignment_4.html', message='insert user!')


# DELETE #
@assignment_4.route('/delete_user', methods=['get', 'POST'])
def delete_user_func():
    user_id = request.form['user_id']
    query = "DELETE FROM users WHERE id='%s';" %user_id
    interact_db(query, query_type='commit')
    return render_template('assignment_4.html', message='delete!')



# update #
@assignment_4.route('/update_user', methods=['GET', 'POST'])
def update_user():
    user_name = request.form['user_name']
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    id = request.form['id']
    query = "UPDATE users SET name ='%s',email ='%s',user_name='%s', password='%s' WHERE id='%s';" % (name, email, user_name, password, id)
    print(query)
    interact_db(query=query, query_type='commit')
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('assignment_4.html', users=users_list, message="changes made!")



@assignment_4.route('/updateuserS', methods=['GET','POST'])
def updateuserS():
    user_id = request.form['user_id']
    print(user_id)
    return render_template('update.html', id=user_id)



@assignment_4.route('/assignment_4/users', methods=['GET'])
def get_users():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    users_array = []
    for user in users_list:
        users_array.append({
            'username': user.user_name,
            'email': user.email,
            'name': user.name
        })
    return jsonify(users_array)


@assignment_4.route('/assignment_4/outer_source', methods=['GET', 'POST'])
def outer_source():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    user_id = request.form['id']
    result = requests.get('https://reqres.in/api/users/' + user_id)
    return render_template('assignment_4.html', user_from_api=result.json()['data'],users=users_list)


@assignment_4.route('/assignment_4/restapi_users/', methods=['GET'])
def get_default_user():
    query = 'select * from users where id=3'
    user = interact_db(query, query_type='fetch')[0]

    return jsonify(user)


@assignment_4.route('/assignment_4/restapi_users/<int:USER_ID>', methods=['GET'])
def get_user(USER_ID):
    query = "select * from users where id='%s'" % USER_ID
    user = interact_db(query, query_type='fetch')[0]
    if user:
        usersdict = {
            'username': user.user_name,
            'email': user.email,
            'name': user.name
        }
        return jsonify(usersdict)
    return jsonify({'Message Error': 'User not found'})