from fastapi import Request
from resources.auth import create_user, verify_captcha
from data.schemas import UserModel, SignupModel
from resources.exceptions import *
from resources.api_responses import APIResponse
from urls import user_router


@user_router.post('/signup', response_model=APIResponse.example_model(UserModel))
async def signup_user(request: Request, user_data: SignupModel):
    await verify_captcha(request.app.redis, user_data.captcha_key, user_data.captcha_answer)
    await create_user(user_data)
    return APIResponse(UserModel(username=user_data.username, fullname=user_data.fullname))
