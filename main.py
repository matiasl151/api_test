from fastapi import FastAPI, HTTPException, Path
from routes.user_routes import router as user_router
from routes.permission_routes import router as permission_router


app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(permission_router, prefix="/permissions", tags=["permissions"])

@app.get("/")
async def root():
    return {"message": "Hola Mundo"}

