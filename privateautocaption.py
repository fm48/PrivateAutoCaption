# Mo Tech YT

import os
import logging
import pyrogram
from config import Config  


if __name__ == "__main__" :
    plugins = dict(
        root="mt_privateautocaption"
    )
    MrktTech = pyrogram.Client(
        "CaptionBot",
        bot_token=Config.MRKT_BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=300
    )
    mrkttech.run()
