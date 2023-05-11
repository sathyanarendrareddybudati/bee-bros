from fastapi import FastAPI,Security, HTTPException,Depends
from database import Base,engine
from routes.users import controllers
from routes.products import controllers as products
from fastapi.security.api_key import APIKeyHeader, APIKey

Base.metadata.create_all(engine)

X_API_KEY = APIKeyHeader(name='x-api-key')

async def api_key_auth(
    api_key_header: str = Security(X_API_KEY),
):
    if api_key_header == 'satya-reddy':
        return api_key_header
    else:
        raise HTTPException(status_code=403)

app = FastAPI(dependencies=[Depends(api_key_auth)],title='bee-bros', openapi_url=f"/openapi.json")
# app = FastAPI()

app.include_router(controllers.router)
app.include_router(products.router)

@app.get("/")
def Home():
    response = "welcome to bee-bros"
    return response