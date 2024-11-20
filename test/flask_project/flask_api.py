from flask import request, jsonify, Blueprint


sub_api = Blueprint('sub_api', __name__)

# 获取学生成绩列表
@sub_api.route('/users/scores', methods=['GET'])
def get_names():
    ID = request.args.get('ID')
    return f"Scores of {ID}"
