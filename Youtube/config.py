import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6618550871:AAFmtxC7gjnxqo5_Qfkrp0yUGBTAECwkRlc")
    API_ID = int(os.environ.get("API_ID", "24267726")
    API_HASH = os.environ.get("API_HASH", "7500ba8248548cc3864bd033668f9a9a")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1002104333488")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
