from flask import request, jsonify, Blueprint


sub_api = Blueprint('sub_api', __name__)

@sub_api.route('/names', methods=['GET'])
def get_names():
    return "List of users"
