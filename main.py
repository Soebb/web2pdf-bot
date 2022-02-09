import os, re, time
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

# {ee}
ee = "م"
s="masum"
e=3
fa="آپارتمان بی گناهان"
x='\"-\"\"-\"\"-\"\"-\"\"-\"\"-\"\"-\"\"-\"\"-\"\"-\"\"-\"\"-\"\"-\"\"-\"\"-\"'
text=f"سریال {s} {fa} قسمت {e} با زیرنویس فارسی" \
     f"\nقسمت {ee} سریال {fa} {s} با زیرنویس چسبیده رایگان" \
     f"\nقسمت {e} سریال {fa} - {s} با زیرنویس فارسی چسبیده دی ال مکوین" \
     f"\nتماشای قسمت بعدی در کانال تلگرام ما :" \
     f"\nhttps://t.me/joinchat/Rguc8ahmI2pnKElU" \
     f"\n,سریال {fa}" \
     f"\n,{fa}" \
     f"\n,{fa}{e}" \
     f"\n,سریال {fa}{e}" \
     f"\n-------------------------" \
     f"\nزیرنویس چسبیده قسمت {e} سریال ترکی {fa} قسمت 54 {s}" \
     f"\nقسمت {e} سریال {fa} با زیرنویس چسبیده قسمت {ee} 54 {s}" \
     f"\nسریال {fa} {e} {s} قسمت {ee} با زینویس چسبیده" \
     f"\nجهت دانلود تماشای کامل این قسمت کانال تلگرام دی ال مکوین شوید :" \
     f"\nhttps://t.me/joinchat/Rguc8ahmI2pnKElU" \
     f"\n,سریال {fa}" \
     f"\n,{fa}" \
     f"\n,{fa}{e}" \
     f",سریال {fa}{e}"



@Bot.on_message(filters.private & filters.text)
async def webtopdf(_, m):
    url = m.text
    name = 'temp/v.mp4'
    opts = {
        'format': 'best[height<=240]',
        'geo_bypass':True,
        'nocheckcertificate':True,
        'videoformat':'mp4',
        'outtmpl':'temp/v.mp4'
    }
    os.system(f'yt-dlp -vU --geo-bypass --no-check-certificate -o "v.mp4" "{url}"')
    #with YoutubeDL(opts) as ytdl:
    #    ytdl.download([url])
    #    ytdl.extract_info(url, download=True)
    time.sleep(30)
    #M=await m.reply_document(name)
    #await M.edit(M.document.file_name)
    os.remove(name)


Bot.run()
