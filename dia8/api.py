from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

# Serializador de saida
class PersonOut(BaseModel):
    id: int
    name: str
    picture: str
    age: int
    email: str
    about: Optional[str] =""
    is_active: bool


app = FastAPI()


@app.get("/", response_model=PersonOut)
async def read_root():
    return PersonOut(
        id=1,
        name="Bruno",
        picture="http://foto.jpg",
        age=15,
        email="bruno@rocha.com",
        about="jsfaassdasd",
        is_active=True
    )


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
