from typing import Annotated, Literal
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field


app = FastAPI()


class FilterParams(BaseModel):
    limit: Annotated[int, Field(gt=0)]
    offset: int
    order_by: Literal["created_at", "updated_at"] = "created_at"


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return {"message": "Todo bien!", **filter_query.model_dump()}
