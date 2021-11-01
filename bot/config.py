# < (c) 2021 @kaif-00z >

from decouple import config


class Var:
    REDIS_URI = config("REDIS_URI", default=None)
    REDIS_PASS = config("REDIS_PASSWORD", default=None)
    API_ID = config("API_ID", default=None, cast=int)
    API_HASH = config("API_HASH", default=None)
    SESSION = config("SESSION", default=None)
