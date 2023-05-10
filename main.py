from fastapi import FastAPI
from database import Base,engine
from routes.users import controllers
from routes.products import controllers as products

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(controllers.router)
app.include_router(products.router)

@app.get("/")
def Home():
    response = "welcome to bee-bros"
    return response