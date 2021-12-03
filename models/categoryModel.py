from flask import Flask
from models import db

class Categories(db.Model):
	__tablename__ = 'categories'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(150), nullable=False)
	description = db.Column(db.Text, nullable=True)
	slug = db.Column(db.String(150), unique=True, nullable=False)
	status = db.Column(db.Boolean, default=False, nullable=False)
	created_on = db.Column(db.DateTime, default=db.func.now())
	updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

	def __init__(self, name, slug, description):
		self.name = name
		self.description = description
		self.slug = slug


