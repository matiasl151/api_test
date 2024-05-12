from fastapi import APIRouter, HTTPException, Path
from models.user import User
from db import fake_db_users as users
from typing import List

router = APIRouter()

@router.get("/", response_model=List[User])
async def read_users():
    return users

@router.get("/{user_id}", response_model=User)
async def read_user(user_id: str = Path(..., title="ID del usuario a obtener")):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.post("/", response_model=User)
async def create_user(user: User):
    # Generar el ID combinando first_name y last_name si no se proporciona
    if not user.id:
        user.id = f"{user.first_name}.{user.last_name}"
        
    # Verificar si el correo electrónico ya está en uso
    if any(existing_user.email == user.email for existing_user in users):
        raise HTTPException(status_code=400, detail="El correo electrónico ya está en uso")
    
    # Agregar el usuario a la base de datos simulada
    users.append(user)
    return user
