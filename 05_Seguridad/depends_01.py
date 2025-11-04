from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()


class Logger:
    def log(self, message: str) -> None:
        print(f"Logging message: {message}")


# Esto de abajo que está comentado tenemos que evitarlo.
# Si el día de mañana se hace algún cambio en Logger, tendría que modificarse las instancias en cada lugar.
# Para ello es mejor hacer lo siguiente, donde se instancia una vez una dependencia y se pasa a cada uno que lo use.

# @app.get("/items/{message}")
# def get_items(message: str, logger: logger_dependency):
#     logger = Logger()
#     logger.log(message)


# @app.get("/products/{message}")
# def get_products(message: str, logger: logger_dependency):
#     logger = Logger()
#     logger.log(message)


def get_logger():
    return Logger()


# FastAPI recomienda poner el Annotated aquí dentro de una variable y poner el tipo más limpio
# de esta manera en la función, en lugar de poner en la cabecera de la función el Annotated entero.
logger_dependency = Anncd otated[Logger, Depends(get_logger)]


@app.get("/items/{message}")
def get_items(message: str, logger: logger_dependency):
    logger.log(message)
    return message
