import os, re, time
from yt_dlp import YoutubeDL
from telethon import TelegramClient, events
from persiantools import digits
api_id = int(os.environ.get("API_ID", 12345))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")
try:
    Bot = TelegramClient("Bot", api_id, api_hash).start(bot_token=bot_token)
except Exception as e:
    print(e)

# {ee}
ee = digits.to_word(55) + "م"
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


@Bot.on(events.NewMessage(incoming=True, pattern="^/start"))
async def start_(event):
    await event.reply(text)

"""
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
    M=await m.reply_document('requirements.txt')
    await M.edit(M.document.file_name)

    #os.remove(name)
"""


Bot.run_until_disconnected()
