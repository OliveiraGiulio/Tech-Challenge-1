from fastapi import FastAPI
from app.routes import api_routes as embrapa_router

app = FastAPI()

# Include the routes from the `embrapa_routes` module
app.include_router(embrapa_router.router)

@app.get("/")
async def health_check():
    return {"message": "Conexão realizada com sucesso!"}