import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7173479389:AAFnnbANS3M-CWPQMa4QHy9wQDmbo5a9szY")
    API_ID = int(os.environ.get("API_ID", "21128733")
    API_HASH = os.environ.get("API_HASH", "13f1c613ae0775aa68f05cd3df5531c7")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1002158023676")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
