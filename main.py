import os, re
import pyppdf
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



dirs = 'dl/'


# Running bot
Bot = Client(
    'PersianSubBot',
    api_id="2421254",
    api_hash="bc8ee680fd4f2720d3a24e43831c90b1",
    bot_token="1946110292:AAETH5cW0tu45xlr_gOyrTGnoUu325XKe34"
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
    text = START_TXT.format(update.from_user.mention)
    reply_markup = START_BTN
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )


@Bot.on_message(filters.private & filters.text)
async def webtopdf(_, m):
    url = m.text
    name = re.sub(r'^\w+://', '', url.lower())
    name = name.replace('/', '-') + '.pdf'
    msg = await m.reply("Processing..")
    try:
        await pyppdf.save_pdf(name, url)
    except:
        return await msg.edit('No access to the network.')
    await m.reply_document(name)
    await msg.delete()
    os.remove(name)



Bot.run()
