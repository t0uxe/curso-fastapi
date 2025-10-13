from fastapi import FastAPI
from pydantic import BaseModel, Field, Literal
from typing import Annotated


app = FastAPI()


# class Tarea(BaseModel):
#     id: Annotated[int, Field(gt=0)]
#     titulo: Annotated[str, Field(ge=3)]
#     estado: []


class Tarea(BaseModel):
    item_id: Annotated[float, Field(gt=0)]
    titulo: Annotated[str, Field(min_length=3)]
    estado: Literal["pendiente", "completado"] = "pendiente"


fake_db: list[Tarea] = [
    Tarea(id=1, titulo="Estudiar Python", estado="pendiente"),
    Tarea(id=2, titulo="Lavar la ropa", estado="completado"),
    Tarea(id=3, titulo="Leer un libro", estado="pendiente"),
    Tarea(id=4, titulo="Ir al gimnasio", estado="completado"),
    Tarea(id=5, titulo="Comprar comida", estado="pendiente"),
    Tarea(id=6, titulo="Limpiar el cuarto", estado="pendiente"),
    Tarea(id=7, titulo="Pagar cuentas", estado="completado"),
    Tarea(id=8, titulo="Llamar a mamá", estado="pendiente"),
    Tarea(id=9, titulo="Revisar correo", estado="pendiente"),
    Tarea(id=10, titulo="Lavar carro", estado="pendiente"),
]
