import os, re, time
from yt_dlp import YoutubeDL
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

Bot = Client(
    "Web2PDF-Bot",
    bot_token = BOT_TOKEN,
    api_id = API_ID,
    api_hash = API_HASH
)
s="masum"
e=3
fa="آپارتمان بی گناهان"
x='\"-\"\"-\"\"-\"\"-\"\"-\"\"-\"\"-\"\"-\"\"-\"\"-\"\"-\"\"-\"\"-\"\"-\"\"-\"'
text=f"سریال {s} {fa} قسمت {e} با زیرنویس فارسی" \
     f"\nقسمت پنجاه و چهارم سریال {fa} {s} با زیرنویس چسبیده رایگان" \
     f"\nقسمت {e} سریال {fa} - {s} با زیرنویس فارسی چسبیده دی ال مکوین" \
     f"\nتماشای قسمت بعدی در کانال تلگرام ما :" \
     f"\nhttps://t.me/joinchat/Rguc8ahmI2pnKElU" \
     f"\n,سریال {fa}" \
     f"\n,{fa}" \
     f"\n,{fa}{e}" \
     f"\n,سریال {fa}{e}" \
     f"\n-------------------------" \
     f"\nزیرنویس چسبیده قسمت {e} سریال ترکی {fa} قسمت 54 {s}" \
     f"\nقسمت {e} سریال {fa} با زیرنویس چسبیده قسمت پنجاه و چهارم 54 {s}" \
     f"\nسریال {fa} {e} {s} قسمت پنجاه و چهارم با زینویس چسبیده" \
     f"\nجهت دانلود تماشای کامل این قسمت کانال تلگرام دی ال مکوین شوید :" \
     f"\nhttps://t.me/joinchat/Rguc8ahmI2pnKElU" \
     f"\n,سریال {fa}" \
     f"\n,{fa}" \
     f"\n,{fa}{e}" \
     f",سریال {fa}{e}"

START_TXT = """
Hi {}, I am web2pdf Bot.

> `I can download webpages as PDF.`

Send any URL to get started.
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Source Code', url='https://github.com/samadii/web2pdf-bot'),
        ]]
    )


@Bot.on_message(filters.command(["start"]))
async def start(bot, update):
    reply_markup = START_BTN
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )


@Bot.on_message(filters.private & filters.text)
async def webtopdf(_, m):
    """
    url = m.text
    name = 'temp/v.mp4'
    opts = {
        'format': 'best[height<=240]',
        'geo_bypass':True,
        'nocheckcertificate':True,
        'videoformat':'mp4',
        'outtmpl':'temp/v.mp4'
    }
    #os.system(f'youtube-dl --geo-bypass --no-check-certificate --add-header "Cookie:t" -o "temp/v.mp4" "{url}"')
    with YoutubeDL(opts) as ytdl:
        #ytdl.download([url])
        ytdl.extract_info(url, download=True)
    time.sleep(30)
    """
    M=await m.reply_document('requirements.txt')
    await M.edit(M.document.file_name)

    #os.remove(name)



Bot.run()
