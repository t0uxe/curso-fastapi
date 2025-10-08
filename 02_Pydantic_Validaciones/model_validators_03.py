# Para las validaciones de modelos, Pydantic tiene estos 3:
# After
# Before
# Wrap
# Y ademas solo por decorador

from typing_extensions import Self
from pydantic import BaseModel, model_validator


class UserModel(BaseModel):
    username: str
    password: str
    password_repeat: str

    @model_validator(mode="after")
    def check_passwords(self) -> Self:
        if self.password != self.password_repeat:
            raise ValueError("Objeto incorrecto: passwords no match.")
        return self


usuario1: UserModel = UserModel(
    username="eduardo", password="1234", password_repeat="12345"
)  # Salta error
