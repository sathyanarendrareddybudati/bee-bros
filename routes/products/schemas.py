from pydantic import BaseModel
from fastapi import UploadFile

class ProductsIN(BaseModel):
    category_id :int
    name : str
    slug : str
    description : str
    image : str
    price : int
    in_stock : bool
    is_active : bool

class CategoryIN(BaseModel):
    id : int
    name : str
    slug : str

class ProductCart(BaseModel):
    product_id : int
    quality : int

class CartIn(BaseModel):
    id : int 
    name : str
    price : int