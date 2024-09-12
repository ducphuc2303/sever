from .model import User 
from .schema import (
    UserSignUpInput
)


class UserService:

    @staticmethod
    def sign_up(data: UserSignUpInput) -> User:
        user = User.objects.create(**data.__dict__)
        user.set_password(data.password) #* mã hóa mật khẩu
        user.save()
        return user