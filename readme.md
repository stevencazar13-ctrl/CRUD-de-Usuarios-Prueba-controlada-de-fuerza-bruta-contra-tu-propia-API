# User Management API

API simple de gestión de usuarios con FastAPI.

## Ejecutar la API

Instalar FastAPI y Uvicorn, luego ejecutar el servidor. La documentación interactiva estará disponible en http://127.0.0.1:8000/docs

## Endpoints disponibles

- **POST /register** - Registrar nuevo usuario
- **GET /List** - Listar todos los usuarios  
- **GET /Search** - Buscar usuario por ID
- **PUT /Update** - Actualizar información de usuario
- **DELETE /Delete** - Eliminar usuario
- **POST /Login** - Iniciar sesión

## Pruebas

### Respuestas exitosas esperadas:
```
POST /register

{
  "id": 1,
  "username": "nombre_usuario",
  "password": "contraseña",
  "email": "email@ejemplo.com",
  "is_active": true
}
GET /List

[
  {
    "id": 1,
    "username": "nombre_usuario",
    "password": "contraseña",
    "email": "email@ejemplo.com",
    "is_active": true
  }
]
GET /Search

{
  "User name": "nombre_usuario",
  "User email": "email@ejemplo.com",
  "Active": true
}
PUT /Update

{
  "message": "User successfully updated",
  "user": {
    "id": 1,
    "username": "nuevo_nombre",
    "password": "contraseña",
    "email": "nuevo_email@ejemplo.com",
    "is_active": false
  }
}
DELETE /Delete

{
  "message": "User deleted successfully"
}
POST /Login

{
  "message": "Successful login"
}
Usar la documentación interactiva en /docs para probar todos los endpoints fácilmente desde el navegador.
