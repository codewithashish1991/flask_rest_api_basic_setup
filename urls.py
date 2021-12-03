from flask import Blueprint
from flask_restful import Api
from controllers.Hello import Hello
from controllers.categoryController import Category, CategoryComments

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# api urls
api.add_resource(Hello, '/check', endpoint="test")

# categories urls
api.add_resource(Category, '/categories', endpoint="categories_list", methods=['GET'])
api.add_resource(Category, '/category/add', endpoint="add_categories", methods=['POST'])
api.add_resource(Category, '/category/<int:category_id>', endpoint="category", methods=['PUT', 'DELETE'])
api.add_resource(Category, '/category/<string:slug>', endpoint="slug_category", methods=['GET'])
api.add_resource(CategoryComments, '/category/<int:category_id>/comments', endpoint="category_comments", methods=['GET'])
api.add_resource(CategoryComments, '/category/<int:category_id>/add_comment', endpoint="add_category_comments", methods=['POST'])
api.add_resource(CategoryComments, '/comment/<int:id>', endpoint="delete_comment", methods=['DELETE'])
