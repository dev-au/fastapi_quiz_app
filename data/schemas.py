from pydantic import BaseModel


class UserModel(BaseModel):
    username: str
    fullname: str


class SignupModel(BaseModel):
    username: str
    fullname: str
    password: str
    password_confirm: str
    captcha_key: str
    captcha_answer: int


class LoginModel(BaseModel):
    username: str
    password: str
    captcha_key: str
    captcha_answer: int


class UserRefreshPasswordModel(BaseModel):
    old_password: str
    new_password: str
    new_password_confirm: str
    captcha_key: str
    captcha_answer: int


class TokenModel(BaseModel):
    access_token: str = None
    refresh_token: str = None


class CaptchaData(BaseModel):
    key: str
    img: str


class QuizData(BaseModel):
    id: int
    name: str
