from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('species', type=str, required=True)
parser.add_argument('personality', type=str, required=True)
parser.add_argument('quote', type=str, required=True)

class villager(Resource):
	def get(self):
		return ''

	def put(self, name):
		return ''

api.add_resource(villager, '/<string:name>')

if __name__ == '__main__':
	app.run(debug=True)
