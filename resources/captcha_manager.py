import base64
import random
import uuid

from aioredis import Redis
from captcha.image import ImageCaptcha


async def generate_captcha(redis: Redis):
    random_number = str(random.randint(10000, 99999))
    image = ImageCaptcha()
    captcha_data = image.generate(random_number)
    captcha_bytes = captcha_data.getvalue()
    captcha_base64 = base64.b64encode(captcha_bytes).decode('utf-8')
    captcha_key = uuid.uuid4().hex
    for i in range(10):
        if await redis.exists(captcha_key):
            captcha_key = uuid.uuid4().hex
        else:
            break
    await redis.set(captcha_key, random_number, 15 * 60)
    return captcha_key, captcha_base64
