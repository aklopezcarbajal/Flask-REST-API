from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/database.db'
db  = SQLAlchemy(app)

class villager(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), unique=True, nullable=False)
	species = db.Column(db.String(20), nullable=False)
	personality = db.Column(db.String(20), nullable=False)
	quote = db.Column(db.Text)

	def __repr__(self):
		return '<Villager %r>' % self.name

#db.create_all()

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('species', type=str, required=True)
parser.add_argument('personality', type=str, required=True)
parser.add_argument('quote', type=str, required=True)

mfields = {
	'id' : fields.Integer,
	'name' : fields.String,
	'personality' : fields.String
	'quote' : fields.Text
}


class villagerList(Resource):
	@marshal_with(mfields)
	def get(self, name):
		result = villager.query.filter_by(name=name).first()
		if not result:
			abort(404, message="Villager doesn't exist")
		return result

	def put(self, name):
		return ''

api.add_resource(villagerList, '/<string:name>')

if __name__ == '__main__':
	app.run(debug=True)
