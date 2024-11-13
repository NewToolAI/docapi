import inspect
from flask import Flask, request, jsonify
from flask_api import sub_api

app = Flask(__name__)
app.register_blueprint(sub_api, url_prefix='/sub_api')


# 获取年级学生列表
@app.route('/users/list', methods=['GET'])
def get_users():
    parmams = request.get_json()
    grade = parmams['grade']
    data = f'List of {grade} students'.split(' ')

    return jsonify(code=0, data=data, error=None)


# @app.route('/users/<int:user_id>', methods=['GET'])
# def get_user(user_id):
#     '''获取用户信息'''
#     return f"User {user_id}"


# 创建学生系统用户
@app.route('/users/create', methods=['POST'])
def create_user():
    params = request.get_json()
    name = params['name']
    age = params['age']
    data = {'name': name, 'age': age}

    return jsonify(code=0, data=data, error=None)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
