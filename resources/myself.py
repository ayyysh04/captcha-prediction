from flask import jsonify
from flask_restful import Resource
import tensorflow as tf

class authorInfo(Resource):

    def get(self):
        return jsonify({
            'author': 'Ayush Yadav',
            'project_name': 'NSUT captcha prediction'
        })
