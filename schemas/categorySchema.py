from marshmallow import Schema, fields, validate
from flask_marshmallow import Marshmallow

ma = Marshmallow()

class CategorySchema(ma.Schema):
	"""docstring for CategorySchama"""
	id = fields.Integer(dump_only=True)
	name = fields.String(required=True)		
	description = fields.String(required=True, validate=validate.Length(3))		
	slug = fields.String(required=True)		
	status = fields.Boolean()		
	created_on = fields.DateTime()		
	updated_on = fields.DateTime()		
