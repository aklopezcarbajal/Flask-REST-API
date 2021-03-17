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
	quote = db.Column(db.String(150))

	def __repr__(self):
		return '<Villager %r>' % self.name

#db.create_all()

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('species', type=str, required=True)
parser.add_argument('personality', type=str, required=True)
parser.add_argument('quote', type=str)

parser_update = reqparse.RequestParser()
parser_update.add_argument('name', type=str)
parser_update.add_argument('species', type=str)
parser_update.add_argument('personality', type=str)
parser_update.add_argument('quote', type=str)

mfields = {
	'id' : fields.Integer,
	'name' : fields.String,
	'species' : fields.String,
	'personality' : fields.String,
	'quote' : fields.String
}

class villagerList(Resource):
	@marshal_with(mfields)
	def get(self, name):
		result = villager.query.filter_by(name=name).first()
		if not result:
			abort(404, message="Villager doesn't exist")
		return result

	@marshal_with(mfields)
	def put(self, name):
		args = parser.parse_args()
		vlg = villager(name=args['name'], species=args['species'], personality=args['personality'], quote=args['quote'])

		db.session.add(vlg)
		db.session.commit()
		return vlg, 201

	@marshal_with(mfields)
	def patch(self, name):
		vlg = villager.query.filter_by(name=name).first()
		if not vlg:
			abort(404, message="Villager doesn't exist")

		args = parser_update.parse_args()

		if args['name']:
			vlg.name = args['name']
		if args['species']:
			vlg.species = args['species']
		if args['personality']:
			vlg.personality = args['personality']
		if args['quote']:
			vlg.quote = args['quote']

		db.session.commit()
		return vlg

	def delete(self, name):
		result = villager.query.filter_by(name=name).first()
		if not result:
			abort(404, message="Villager doesn't exist")
		db.session.delete(result)
		db.session.commit()
		print('Deleting...')
		return '', 204



api.add_resource(villagerList, '/villager/<string:name>')

if __name__ == '__main__':
	app.run(debug=True)
