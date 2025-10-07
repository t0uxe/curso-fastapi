from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    id: int
    nombre: str
    email: str
    edad: int | None = None
    activo: bool


app = FastAPI()


@app.get("/users/")
def get_users():
    pass


@app.post("/users/")
def create_user(user: User):
    return {
        "mensaje": f"Usuario {user.nombre.capitalize()} creado exitosamente.",
        "datos": user,
    }


@app.put("/users/{user_id}")
def update_user(user_id: int, user: User, q: str | None = None):
    result: dict = {"user_id": user_id, **user.model_dump()}
    if q:
        result.update({"q": q})
    return result
