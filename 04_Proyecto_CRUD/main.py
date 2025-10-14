from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Annotated, Literal


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


class Tarea(BaseModel):
    id: Annotated[float, Field(gt=0)]
    titulo: Annotated[str, Field(min_length=3)]
    estado: Literal["pendiente", "completado"] = "pendiente"


class FilterParams(BaseModel):
    limit: Annotated[int, Field(ge=1)] = 5
    offset: Annotated[int, Field(ge=0)] = 0
    estado: Literal["pendiente", "completado"] | None = None


app = FastAPI()


@app.get("/tareas/")
async def get_tareas(filter: Annotated[FilterParams, Query()]):
    tareas_filtradas = (
        [tarea for tarea in fake_db if tarea.estado == filter.estado]
        if filter.estado
        else fake_db
    )

    return tareas_filtradas[filter.offset : filter.offset + filter.limit]
