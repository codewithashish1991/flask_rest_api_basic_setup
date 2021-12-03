from flask import request
from flask_restful import Resource
from models import db
from models.categoryModel import Categories
from models.commentsModel import Comments
from schemas.categorySchema import CategorySchema
from schemas.commentsSchema import CommentsSchema

categories_schema = CategorySchema(many=True)
category_schema = CategorySchema()
comment_schema = CommentsSchema()
comments_schema = CommentsSchema(many=True)

class Category(Resource):
	"""docstring for Category"""
	def get(self, slug=''):
		if not slug:
			categories = Categories.query.all()
			data = categories_schema.dump(categories).data
		else:
			category = Categories.query.filter_by(slug=slug).first()
			data = category_schema.dump(category).data

		return {'status': 'success', 'data': data}, 200

	def post(self):
		json_data = request.json
		if not json_data:
			return {'message': 'No input data provided'}, 400
		data, errors = category_schema.load(json_data)
		if errors:
			return errors, 422

		category = Categories.query.filter_by(slug=data['slug']).first()
		if category:
			return {'message': 'Category already exists'}, 400

		category = Categories(
			json_data['name'], json_data['slug'], json_data['description']
		)
		db.session.add(category)
		db.session.commit()
		result = category_schema.dump(category).data

		return { "status": 'success', 'data': result }, 201

	def put(self, category_id):
		json_data = request.json
		if not json_data:
			return {'message': 'No input data provided'}, 400
		data, errors = category_schema.load(json_data)
		if errors:
			return errors, 422
		category = Categories.query.filter_by(id=category_id).first()
		if not category:
			return {'message': 'Category does not exist'}, 400

		category.name = json_data['name']
		category.slug = json_data['slug']
		category.description = json_data['description']
		db.session.commit()
		result = category_schema.dump(category).data
		return { "status": 'success', 'data': result }, 200

	def delete(self, category_id):
		if not category_id:
			return {'message': 'No category id provided'}, 400
		exist_cat = Categories.query.filter_by(id=category_id).first()
		if not exist_cat:
			return {'message': 'Category does not exist'}, 400

		category = Categories.query.filter_by(id=category_id).delete()
		db.session.commit()
		result = category_schema.dump(exist_cat).data
		return { "status": 'success', 'message': 'Category deleted successfully'}, 200


class CategoryComments(Resource):
	"""docstring for CategoryComments"""
	def get(self, category_id):
		if not category_id:
			return {'message': 'category id does not exist in url'}, 400

		exist_cat = Categories.query.filter_by(id=category_id).first()
		
		if not exist_cat:
			return {'message': 'Category does not exist'}, 400
		comments = Comments.query.filter_by(category_id=category_id).all()
		comments = comments_schema.dump(comments).data

		return {'status': 'success', 'data': comments}, 200

	def post(self, category_id):
		json_data = request.json

		if not category_id:
			return {'message': 'category id does not exist in url'}, 400
		exist_cat = Categories.query.filter_by(id=category_id).first()

		if not json_data:
			return {'message': 'No input data provided'}, 400
		
		if not exist_cat:
			return {'message': 'Category does not exist'}, 400

		post_data = {}
		post_data['category_id'] = category_id
		post_data['comments'] = json_data['comments']

		data, errors = comment_schema.load(post_data)
		if errors:
			return errors, 42

		comment = Comments(
			json_data['comments'], category_id
		)
		db.session.add(comment)
		db.session.commit()
		result = comment_schema.dump(comment).data

		return { "status": 'success', 'data': result }, 201

	def delete(self, id):
		if not id:
			return {'message': 'No comment id provided'}, 400
		comment_exist = Comments.query.filter_by(id=id).first()
		if not comment_exist:
			return {'message': 'Comment does not exist'}, 400

		comment = Comments.query.filter_by(id=id).delete()
		db.session.commit()
		result = comment_schema.dump(comment_exist).data
		return { "status": 'success', 'message': 'Comment deleted successfully'}, 200
