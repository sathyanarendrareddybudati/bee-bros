from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DECIMAL,DateTime, text, VARCHAR
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from slugify import slugify

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, nullable=True)
    name = Column(String(255), unique=True, nullable=True)
    slug = Column(String(255), unique=True, nullable=True)

    def __repr__(self):
        return f"Category(id={self.id}, name='{self.name}')"

class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    category=relationship('Category',foreign_keys='Products.category_id')
    name = Column(String(255))
    slug = Column(String(255))
    description = Column(String(255))
    image = Column(String(255))
    price = Column(Integer)
    in_stock = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True)
    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, default=func.now(), onupdate=func.now())

    # def __init__(self, name):
    #     self.name = name
    #     self.slug = slugify(self.name)

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}')"
    
    
class ProductsCart(Base):
    __tablename__ = 'products_cart'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    cart_id = relationship('Products', foreign_keys=[product_id])
    quality = Column(Integer)