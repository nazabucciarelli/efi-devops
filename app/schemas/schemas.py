from marshmallow import fields
from app import ma

class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String()
    password = fields.String()

class CategorySchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()

class ProductSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    category_id = fields.Integer()
    price = fields.Float()
    added_by = fields.Integer()

