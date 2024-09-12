from ninja import ModelSchema, Schema, Field
from .model import (
    User,
)

class UserSignUpInput(ModelSchema):
    # message: str = Field(max_length=500)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )