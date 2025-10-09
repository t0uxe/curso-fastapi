from fastapi import FastAPI, Query
from typing import Annotated


app = FastAPI()


# VALIDACIONES PARA STRINGS
# max_length
# min_length
# pattern


@app.get("/items/")
async def read_items(
    q: Annotated[list[str] | None, Query(max_length=3)] = None,
):
    results: dict = {"mensaje": "Acceso a get(read_items)"}
    if q:
        results.update({"q": q})
    return results
