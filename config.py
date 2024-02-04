import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5892748077:AAFvofY_-6du_89K56vSp0H9ZWxAAtrWrvw")

    APP_ID = int(os.environ.get("APP_ID", 10920209))

    API_HASH = os.environ.get("API_HASH", "16e40a84635f770e382417b71be6f268")
