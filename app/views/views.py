from app import app, db

from flask import (
    jsonify,
    request
)
from flask.views import MethodView
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    get_jwt_identity,
    jwt_required
)
from app.models.models import (
    User,
    Category,
    Product)
from app.schemas.schemas import (
    UserSchema,
    ProductSchema,
    CategorySchema
)

class UserAPI(MethodView):
    def get(self,user_id=None):
        if user_id is None:
            users = User.query.filter_by(visible = 1).all()
            users_schema = UserSchema().dump(users,many=True)
            return jsonify(users_schema)
        user = User.query.get(user_id)
        user_schema = UserSchema().dump(user)
        return jsonify(user_schema)
        
    def post(self):
        user_json = UserSchema().load(request.json) 
        username = user_json.get('username')
        password = user_json.get('password')
        new_user= User(username=username,password=password,visible=1)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(msg=f"User {new_user} added")
    
    def put(self, user_id):
        user = User.query.get(user_id)
        user_json= UserSchema().load(request.json)
        username = user_json.get("username")
        password = user_json.get("password")
        user.username = username
        user.password = password
        db.session.commit()
        user_schema = UserSchema().dump(user)
        return jsonify(user_schema)
    
    def delete(self, user_id):
        user = User.query.get(user_id)
        user.visible = 0
        db.session.commit()
        return jsonify(msg=f"User id {user_id} deleted")
    
class CategoryAPI(MethodView):
    def get(self,category_id=None):
        if category_id is None:
            categories = Category.query.filter_by(visible = 1).all()
            categories_schema = CategorySchema().dump(categories,many=True)
            return jsonify(categories_schema)
        category = Category.query.get(category_id)
        category_schema = CategorySchema().dump(category)
        return jsonify(category_schema)
        
    def post(self):
        category_json = CategorySchema().load(request.json) 
        name = category_json.get('name')
        new_category= Category(name=name,visible=1)
        db.session.add(new_category)
        db.session.commit()
        return jsonify(msg=f"Category {new_category} added")
    
    def put(self, category_id):
        category = Category.query.get(category_id)
        category_json = CategorySchema().load(request.json)
        name = category_json.get("name")
        category.name = name
        db.session.commit()
        category_schema = CategorySchema().dump(category)
        return jsonify(category_schema)
    
    def delete(self, category_id):
        category = Category.query.get(category_id)
        category.visible = 0
        db.session.commit()
        return jsonify(msg=f"Category id {category_id} deleted")
    
class ProductAPI(MethodView):
    def get(self,product_id=None):
        if product_id is None:
            products = Product.query.filter_by(visible = 1).all()
            products_schema = ProductSchema().dump(products,many=True)
            return jsonify(products_schema)
        product = Product.query.get(product_id)
        product_schema = ProductSchema().dump(product)
        return jsonify(product_schema)
        
    def post(self):
        product_json = ProductSchema().load(request.json) 
        name = product_json.get('name')
        category_id = product_json.get('category_id')
        user_id = product_json.get('added_by')
        price = product_json.get('price')
        new_product= Product(name=name,category_id=category_id,price=price,added_by=user_id,visible=1)
        db.session.add(new_product)
        db.session.commit()
        return jsonify(msg=f"Product {new_product} added")
    
    def put(self, product_id):
        product = Product.query.get(product_id)
        product_json = ProductSchema().load(request.json)
        name = product_json.get("name")
        category_id = product_json.get("category_id")
        price = product_json.get('price')
        product.name = name
        product.category_id = category_id
        product.price = price
        db.session.commit()
        product_schema = ProductSchema().dump(product)
        return jsonify(product_schema)
    
    def delete(self, product_id):
        product = Product.query.get(product_id)
        product.visible = 0
        db.session.commit()
        return jsonify(msg=f"Product id {product_id} deleted")

app.add_url_rule("/user",view_func=UserAPI.as_view('user'))
app.add_url_rule("/user/<user_id>", view_func=UserAPI.as_view('user_id'))
app.add_url_rule("/category",view_func=CategoryAPI.as_view('category'))
app.add_url_rule("/category/<category_id>", view_func=CategoryAPI.as_view('category_id'))
app.add_url_rule("/product",view_func=ProductAPI.as_view('product'))
app.add_url_rule("/product/<product_id>", view_func=ProductAPI.as_view('product_id'))