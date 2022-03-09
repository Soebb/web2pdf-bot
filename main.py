import os, re, time, json
from yt_dlp import YoutubeDL
from pyrogram import Client, filters

API_HASH = os.environ['API_HASH'] # Api hash
API_ID = os.environ['API_ID'] # Api id/App id
BOT_TOKEN = os.environ['BOT_TOKEN'] # Bot token

dirs = 'dl/'


# Running bot
Bot = Client(
    'PersianSubBot',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@Bot.on_message(filters.private & filters.text)
async def webtopdf(_, m):
    url = m.text
    name = 'temp/v.mp4'
    opts = {
        'format':'best[height<=240]',
        'verbose':True,
        'geo_bypass':True,
        'nocheckcertificate':True,
        'videoformat':'mp4',
        'outtmpl':'temp/v.mp4'
    }
    #os.system(f'yt-dlp -vU --geo-bypass --no-check-certificate -o "v.mp4" "{url}"')
    with YoutubeDL(opts) as ytdl:
        #ytdl.download([url])
        info = ytdl.extract_info(url, download=False)
    time.sleep(30)
    info = json.dumps(info)
    try:
        await m.reply(info[:4000])
    except Exception as e:
        await m.reply(e)
    #await m.reply_document(name)
    #await M.edit(M.document.file_name)
    os.remove(name)


Bot.run()
