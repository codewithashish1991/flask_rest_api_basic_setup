from marshmallow import Schema, fields, validate
from flask_marshmallow import Marshmallow

ma = Marshmallow()

class CommentsSchema(ma.Schema):
	"""docstring for CommentsSchema"""
	
	id = fields.Integer(dump_only = True)
	comments = fields.String(required=True, validate=validate.Length(8))
	category_id = fields.Integer(required=True)
	status = fields.Boolean()
	created_on = fields.DateTime()
	updated_on = fields.DateTime()
		
