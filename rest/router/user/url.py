from ninja import Router
from rest import Request
from .schema import (
    UserSignUpInput,
)
from .service import (
    UserService
)

user_router = Router(
    tags=['User API']
)


@user_router.post(
    path='/sign-up'
)
def sign_up(request: Request, data_input: UserSignUpInput):
    user = UserService.sign_up(data_input)
    return {
        'username': user.username,
        'password': user.password
    }