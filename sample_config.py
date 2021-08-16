HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SESSION_STRING = environ[
        "SESSION_STRING"
    ]  # Check Readme for session
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    CHAT_ID = int(environ["CHAT_ID"])
    DEFAULT_SERVICE = environ.get("DEFAULT_SERVICE") or "youtube"
    BITRATE = int(environ["BITRATE"])

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 2316698
    API_HASH = "5178f2c2ce9a7d55e6bd9df407dcc71e"
    ARQ_API_KEY = "UULQAB-YNDQXF-KPXGBY-IIKNGP-ARQ"
    CHAT_ID = -1001478147133
    DEFAULT_SERVICE = "youtube"  # Must be one of "youtube"/"saavn"
    BITRATE = 512 # Must be 512/320
    SESSION_STRING = "BQC2x_z0dh21OdGjLp9nxjCjYuzhzszqcwcqKgdfsDgl53slPnDh-F3Ze4tPCrWf3B9FVBtjaw5c489vgT0Uinpki4uwA0u7k0yDURWlO0b_3jT5bouaFS8LSPB44UVox1voyguaqoV-DigYdkA1gr-IWz8kWT4PAcElFNyPlSNPXKiBZfk0_5uEgz5OICxNUpR3DnBBphtKxw8nPgLo5XpgJD5LAoEiWPNMeG4HX_ZOG4R8NSsMHpBo4aHN8cEk2AHISU3WVeA9zEB5ta7JEdBoQ_7BT3qrZEm5DdvNHhH7-zFCsENOJnpq6udPEpTCJ38tsBfGXF0h2GIyZn9LnoSQVbAYbwA"
# don't make changes below this line
ARQ_API = "https://thearq.tech"
