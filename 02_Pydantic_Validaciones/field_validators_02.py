# After: corre despues de validaciones/transformaciones de pydantic
# Before: corre antes de las validaciones/transformaciones de pydantic
# Plain: similar a before, termina al retornar el valor
# Wrap: flexible antes o despues de las validaciones de pydantic

from pydantic import AfterValidator, BaseModel, field_validator
from typing import Annotated


# =================== ANNOTATED ===================
def es_par(value: int) -> int:
    if value % 2 == 1:
        raise ValueError(f"{value} no es número par.")
    return value


NumeroPar = Annotated[int, AfterValidator(es_par)]


class Model1(BaseModel):
    my_number: NumeroPar


class Model2(BaseModel):
    other_number: Annotated[NumeroPar, AfterValidator(lambda v: v + 2)]


class Model3(BaseModel):
    lista_pares: list[NumeroPar]


# ejemplo: Model1 = Model1(my_number=3)
# ejemplo2: Model2 = Model2(other_number=4)
# print(ejemplo2)

# ejemplo3: Model3 = Model3(lista_pares=[2, 5, 10])
# print(ejemplo3)


# =================== DECORATOR ===================
class Item(BaseModel):
    item_id: int
    price: float

    @field_validator(
        "item_id", "price", mode="after"
    )  # mode="before" tambien se puede poner
    def check_positive(cls, value: int | float):
        """Hace la comprobación del valor al crear la instancia del objeto"""
        if value < 0:
            raise ValueError("Item ID debe ser positivo.")
        return value


banana: Item = Item(item_id=2, price=2.7)
