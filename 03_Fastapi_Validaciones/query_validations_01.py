from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import AfterValidator


app = FastAPI()


# VALIDACIONES PARA STRINGS
# max_length
# min_length
# pattern

# METADATA
# title
# description
# alias
# deprecated


def check_valid_id(id: str):
    if id % 2 != 0:
        raise ValueError("Necesita ser par")
    return id


# Validacion para un valor mayor que X
@app.get("/items/")
async def read_items(
    q: Annotated[
        int | None,
        Query(
            gt=3,
            title="Query",
            description="Lo que se va a buscar",
            alias="item-query",
            deprecated=True,
        ),  # Añadida metadata a Query
    ] = None,
):
    results: dict = {"mensaje": "Acceso a get(read_items)"}
    if q:
        results.update({"q": q})
    return results


# # Validacion personalizada
# @app.get("/items/")
# async def read_items(
#     q: Annotated[int | None, AfterValidator(check_valid_id)] = None,
# ):
#     results: dict = {"mensaje": "Acceso a get(read_items)"}
#     if q:
#         results.update({"q": q})
#     return results
