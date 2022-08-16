from flask import jsonify, request
from flask_restful import Resource


class authorInfo(Resource):

    def get(self):
        return jsonify({
            'author': 'Ayush Yadav',
            'project_name': 'NSUT captcha prediction'
        })
