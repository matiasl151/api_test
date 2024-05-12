from fastapi import APIRouter, HTTPException, Path
from typing import List

from models.permission import Permission
from db import fake_db_permissions as permissions

router = APIRouter()

@router.get("/", response_model=List[Permission])
async def read_permissions():
    return permissions

@router.get("/{permission_id}", response_model=Permission)
async def read_permission(permission_id: int = Path(..., title="ID del permiso a obtener")):
    permission = next((permission for permission in permissions if permission["id"] == permission_id), None)
    if permission is None:
        raise HTTPException(status_code=404, detail="Permiso no encontrado")
    return permission

@router.post("/", response_model=Permission)
async def create_permission(permission: Permission):
    
    # Verificar si el ID del permiso esta en uso
    if any(existing_permission.id == permission.id for existing_permission in permissions):
        raise HTTPException(status_code=400, detail="El ID del permiso ya esta en uso")

    # Agregar el permiso a la base de datos simulada
    permissions.append(permission)
    return permission

