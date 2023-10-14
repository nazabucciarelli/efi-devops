from app import db
from sqlalchemy import ForeignKey, DateTime

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True,nullable=False)
    password = db.Column(db.String(20), nullable=False)
    visible = db.Column(db.Boolean, default=True, nullable=False)

    def __str__(self) -> str:
        return self.username
    
class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True,nullable=False)
    category_id = db.Column(db.Integer,ForeignKey("category.id"), nullable=False)
    price = db.Column(db.Double, nullable=False)
    added_by = db.Column(db.Integer,ForeignKey("user.id"), nullable=False)
    visible = db.Column(db.Boolean, default=True, nullable=False)

    def __str__(self) -> str:
        return self.name
    
class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True,nullable=False)
    visible = db.Column(db.Boolean, default=True, nullable=False)

    def __str__(self) -> str:
        return self.name