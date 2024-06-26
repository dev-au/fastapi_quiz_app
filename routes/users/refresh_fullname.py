from data.schemas import UserRefreshFullnameModel
from resources.api_response import APIResponse
from resources.authentication import *
from resources.depends import CurrentUser
from resources.error_docs import error_docs
from urls import user_router


@error_docs(OldPasswordIncorrectException, FullnameValidationException)
@user_router.patch('/change-fullname', response_model=APIResponse.example_model())
async def change_user_fullname(user: CurrentUser, user_data: UserRefreshFullnameModel):
    if not verify_password(user_data.password, user.hashed_password):
        raise OldPasswordIncorrectException()
    validate_fullname(user_data.new_fullname)
    user.fullname = user_data.new_fullname
    await user.save()
    return APIResponse()
