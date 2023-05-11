from database import get_database_session
from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm import Session
from .models import Products,Category,ProductsCart
from .schemas import ProductsIN,CategoryIN,CartIn,ProductCart

router = APIRouter(
    tags=['PRODUCTS'],
)

@router.get('/products/{product_id}')
def products(product_id:int, db:Session=Depends(get_database_session)):

    cxt = {}
    products = db.query(Products).filter(Products.id==product_id).first()

    cxt['product_id'] = products.id
    cxt['product_name'] = products.name
    cxt['category'] = products.category_id
    cxt['description'] = products.description
    cxt['price'] = products.price
    cxt['image'] = products.image
    cxt['in_stock'] = products.in_stock

    return {"results":cxt}

@router.post('/products/create')
def product_create(product:ProductsIN, db:Session=Depends(get_database_session)):
    products = Products(**product.dict())
    db.add(products)
    db.commit()
    db.refresh(products)
    return products

@router.post('/category/create')
def category_create(category:CategoryIN, db:Session=Depends(get_database_session)):
    categorys = Category(**category.dict())
    db.add(categorys)
    db.commit()
    db.refresh(categorys)
    return categorys

@router.post('/cart/create')
def cart_create(cart:CartIn, db:Session=Depends(get_database_session)):
    carts = Category(**cart.dict())
    db.add(carts)
    db.commit()
    db.refresh(carts)
    return carts

@router.post('/get/product/cart',status_code=status.HTTP_200_OK)
def get_product_cart(carts: ProductCart, db: Session = Depends(get_database_session)):
    product = db.query(Products).get(carts.product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    new_cart_item = ProductsCart(product_id=carts.product_id, quality=carts.quality)
    db.add(new_cart_item)
    db.commit()
    db.refresh(new_cart_item)