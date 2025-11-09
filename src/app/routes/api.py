from flask import Blueprint, request, jsonify

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/calc-area', methods=['POST'])
def calc_area():
    data = request.get_json()
