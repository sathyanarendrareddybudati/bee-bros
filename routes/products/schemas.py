from pydantic import BaseModel
from fastapi import UploadFile

class ProductsIN(BaseModel):
    category_id :int
    name : str
    slug : str
    description : str
    image : UploadFile
    price : int
    in_stock : bool
    is_active : bool

class CategoryIN(BaseModel):
    id : int
    name : str
    slug : str