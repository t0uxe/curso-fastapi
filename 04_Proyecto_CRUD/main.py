from fastapi import FastAPI, Query, HTTPException, Path
from pydantic import BaseModel, Field
from typing import Annotated, Literal
from itertools import count

id_generator: int = count(start=1)


def obtener_nuevo_id() -> int:
    return next(id_generator)


class TareaBase(BaseModel):
    titulo: Annotated[str, Field(min_length=3)]
    estado: Literal["pendiente", "completado"] = "pendiente"


class TareaUpdate(BaseModel):
    titulo: Annotated[str, Field(min_length=3)]
    estado: Literal["pendiente", "completado"]


class TareaCreate(TareaBase):
    pass


class Tarea(TareaBase):
    id: Annotated[int, Field(gt=0)]


class FilterParams(BaseModel):
    limit: Annotated[int, Field(ge=1)] = 5
    offset: Annotated[int, Field(ge=0)] = 0
    estado: Literal["pendiente", "completado"] | None = None
    search: Annotated[str, Field()] | None = None


fake_db: list[Tarea] = [
    Tarea(id=obtener_nuevo_id(), titulo="Estudiar Python", estado="pendiente"),
    Tarea(id=obtener_nuevo_id(), titulo="Lavar la ropa", estado="completado"),
    Tarea(id=obtener_nuevo_id(), titulo="Leer un libro", estado="pendiente"),
    Tarea(id=obtener_nuevo_id(), titulo="Ir al gimnasio", estado="completado"),
    Tarea(id=obtener_nuevo_id(), titulo="Comprar comida", estado="pendiente"),
    Tarea(id=obtener_nuevo_id(), titulo="Limpiar el cuarto", estado="pendiente"),
    Tarea(id=obtener_nuevo_id(), titulo="Pagar cuentas", estado="completado"),
    Tarea(id=obtener_nuevo_id(), titulo="Llamar a mamá", estado="pendiente"),
    Tarea(id=obtener_nuevo_id(), titulo="Revisar correo", estado="pendiente"),
    Tarea(id=obtener_nuevo_id(), titulo="Lavar carro", estado="pendiente"),
]


app = FastAPI()


@app.get("/tareas/", response_model=list[Tarea])
async def get_tareas(filter: Annotated[FilterParams, Query()]) -> list[Tarea]:
    tareas_filtradas = (
        [tarea for tarea in fake_db if tarea.estado == filter.estado]
        if filter.estado
        else fake_db
    )

    if filter.search:
        tareas_filtradas = [
            tarea
            for tarea in tareas_filtradas
            if filter.search.lower() in tarea.titulo.lower()
        ]

    return tareas_filtradas[filter.offset : filter.offset + filter.limit]


@app.get("/tareas/{id}", response_model=Tarea)
async def get_tarea(id: Annotated[int, Path(ge=0)]):
    for tarea in fake_db:
        if id == tarea.id:
            return tarea
    raise HTTPException(status_code=404, detail="ID no encontrado.")


@app.post("/tareas/", response_model=Tarea, status_code=201)
async def create_tarea(tarea: TareaCreate):
    nuevo_id: int = obtener_nuevo_id()
    nueva_tarea: Tarea = Tarea(id=nuevo_id, **tarea.model_dump())
    fake_db.append(nueva_tarea)
    return nueva_tarea


@app.put("/tareas/{id}", response_model=Tarea)
async def actualizar_tarea(id: Annotated[int, Path(gt=0)], tarea_update: TareaUpdate):
    for i, tarea in enumerate(fake_db):
        if tarea.id == id:
            tarea_actualizada = tarea.model_copy(update=tarea_update.model_dump())
            fake_db[i] = tarea_actualizada
            return tarea_actualizada
    raise HTTPException(
        status_code=404, detail=f"No se ha encontrado la tarea con el ID {id}."
    )
