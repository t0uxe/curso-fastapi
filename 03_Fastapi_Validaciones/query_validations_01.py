from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import AfterValidator


app = FastAPI()


# VALIDACIONES PARA STRINGS
# max_length
# min_length
# pattern


def check_valid_id(id: str):
    if id % 2 != 0:
        raise ValueError("Necesita ser par")
    return id


# Mira que el valor sea mayor que 3
# @app.get("/items/")
# async def read_items(
#     q: Annotated[int | None, Query(gt=3)] = None,
# ):
#     results: dict = {"mensaje": "Acceso a get(read_items)"}
#     if q:
#         results.update({"q": q})
#     return results

# Validacion para un valor mayor que X
# @app.get("/items/")
# async def read_items(
#     q: Annotated[int | None, Query(gt=3)] = None,
# ):
#     results: dict = {"mensaje": "Acceso a get(read_items)"}
#     if q:
#         results.update({"q": q})
#     return results


# Validacion personalizada
@app.get("/items/")
async def read_items(
    q: Annotated[int | None, AfterValidator(check_valid_id)] = None,
):
    results: dict = {"mensaje": "Acceso a get(read_items)"}
    if q:
        results.update({"q": q})
    return results
