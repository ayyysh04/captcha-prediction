from genericpath import exists
from flask import jsonify, request
from flask_restful import Resource
from resources.solve_captchas import solve_captcha
import base64
import os


class getCaptcha(Resource):

    def get(self):
        try:
            json_data = request.get_json()
            if(json_data == None):
                return jsonify({"error": "params not found"})

            base64Image = json_data['image']
            pw = json_data['temp']
            if(base64Image == None or pw == None):
                return jsonify({"error": "params not found"})
            with open("resources/temp.jpg", "wb") as fh:
                fh.write(base64.b64decode(base64Image))
            captcha = solve_captcha()
            if(exists("resources/temp.jpg") == True):
                print("yess")
                os.remove("resources/temp.jpg")
            return jsonify({"captcha": captcha})
        except:
            print('An exception occurred')
