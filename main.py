from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.myself import authorInfo
from resources.captchaService import getCaptcha

app = Flask(__name__)
api = Api(app)

CORS(app)


api.add_resource(authorInfo, '/')
api.add_resource(getCaptcha, '/getCaptcha')

if __name__ == '__main__':
    app.run(debug=False)
