# <C> MrktTech


import os

class Config(object):
    MRKT_BOT_TOKEN = os.environ.get("MRKT_BOT_TOKEN", "")
    API_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    CAPTION = os.environ.get("CAPTION", "@Mrkt_Tech @Mrkt_Tech_Group")
    BUTTON_TEXT = os.environ.get("BUTTON", "🔻Join Channel🔻")
    URL_LINK = os.environ.get("LINK", "T.ME/MRKT_TECH")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
