from fastapi import FastAPI

app = FastAPI()

# Dos rutas iguales, siempre se coge la primera.


# Rutas fijas siempre al principio
@app.get("/books/favorite")
async def get_favorite_book():
    return {"title": "1984"}


@app.get("/books/{book_id}")
async def root(book_id: int):
    return {"book_id": book_id}
