from sys import prefix
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep
from random import randint

app = Client("my_account")

@app.on_message(filters.command("ufo", prefixes="/"))
async def main(client,message):
    try:
        for _ in range(0,101,5):
            await message.edit("Поиск данных об НЛО "+str(_)+"%")
        is_ufo = randint(0,1)
        
        if is_ufo==False:
            await message.reply_text("👽 не найдено в этом чате. Поищу в других")
        else:
            await message.reply_text("найдено одно неопознанное 👽 в этом чате. "+str(message["chat"]["first_name"]) or " " + " " +str(message["chat"]["last_name"]) or " ")
    except FloodWait as e:
        sleep(e.x)

@app.on_message(filters.command("repeat", prefixes="/") & filters.me)
async def repeat(client,message):
    try:
        repeat_count = message.text.split(' ')
        repeat_count = int(repeat_count[-1])
        output_text = message.text.split("/repeat ", maxsplit=1)[1]
        output_text = output_text.split(' ')[:-1]

        await message.edit(' '.join(output_text))
        for i in range(repeat_count-1):
            await message.reply_text(' '.join(output_text))
    except FloodWait as e:
        sleep(e.x)

@app.on_message(filters.command("info", prefixes="/"))
async def type(client, message):
    print(client)
    print(message)
    
app.run()