# After: corre despues de validaciones/transformaciones de pydantic
# Before: corre antes de las validaciones/transformaciones de pydantic
# Plain: similar a before, termina al retornar el valor
# Wrap: flexible antes o despues de las validaciones de pydantic

from fastapi import FastAPI
from pydantic import AfterValidator, BaseModel
from typing import Annotated


def es_par(value: int) -> int:
    if value % 2 == 1:
        raise ValueError(f"{value} no es número par.")
    return value


NumeroPar = Annotated[int, AfterValidator(es_par)]


class Model1(BaseModel):
    my_number: NumeroPar


ejemplo: Model1 = Model1(my_number=3)

# class Model2(BaseModel):
# class Model3(BaseModel):
