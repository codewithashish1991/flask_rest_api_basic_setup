from flask import Flask
from models import db

class Comments(db.Model):
	"""docstring for Comments"""
	__tablename__ = 'comments'

	id = db.Column(db.Integer, primary_key=True)
	comments = db.Column(db.String(200), nullable=False)
	category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
	category = db.relationship('Categories',backref=db.backref('comments', lazy='dynamic'))
	
	def __init__(self, comments, category_id):
		self.comments = comments
		self.category_id = category_id
