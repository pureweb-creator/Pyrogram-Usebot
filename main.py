from sys import prefix
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep
from datetime import datetime
import glob,random
from random import randint
import re
import uuid
import config as cfg

app = Client("my_account")

@app.on_message(filters.command("ufo", prefixes="/"))
async def ufo(_,message):
    try:
        for i in range(0,101,5):
            await message.edit("Поиск данных об НЛО "+str(i)+"%")
        is_ufo = randint(0,1)
        
        if is_ufo==False:
            await message.reply_text("👽 не найдено в этом чате. Поищу в других")
        else:
            await message.reply_text("найдено одно неопознанное 👽 в этом чате. "+str(message["chat"]["first_name"]) or " " + " " +str(message["chat"]["last_name"]) or " ")
    except FloodWait as e:
        sleep(e.x)

@app.on_message(filters.command("repeat", prefixes="/"))
async def repeat(_,message):
    try:
        repeat_count = message.text.split(' ')
        repeat_count = int(repeat_count[-1])
        output_text = message.text.split("/repeat ", maxsplit=1)[1]
        output_text = output_text.split(' ')[:-1]

        await message.edit(' '.join(output_text)+" 1")
        for i in range(repeat_count-1):
            await message.reply_text(' '.join(output_text) + " " + str(i+2))
    except FloodWait as e:
        sleep(e.x)

@app.on_message(filters.command("type", prefixes="/") & filters.me)
async def type(_,message):
    try:
        input_message = message.text.split("/type")[1].strip()
        output_message = ""
        for i in range(len(input_message)):
            output_message+=input_message[i]
            await message.edit(output_message+"|")
        await message.edit(output_message)
    except FloodWait as e:
        sleep(e.x)

f = open('src/cats.txt',encoding='utf-8',mode='r')
cats = f.read()
cats = cats.split(',')

@app.on_message(filters.user(cfg.allowed_users))
async def main(client, message):
    try:
        if(message.animation):   
            file_name = str(datetime.datetime.now().date()+"_"+datetime.datetime.now().time().replace(":",".")+uuid.uuid4().hex)
            await client.download_media(message,file_name+".mp4")
            await message.reply_text('Спасибо за сотрудничество!👊 Кот был добавлен в общую базу всех котов. 😼')
        if(message.text):
            ''' send random cat image '''
            input_message = re.split('[-+# ,.!@$%^&*()]', message.text)
            input_message = [msg.lower() for msg in input_message]

            if set(input_message) & set(cats):
                images = glob.glob(random.choice(cfg.file_path_type))
                random_image = random.choice(images)
                await message.reply_animation(random_image)

    except FloodWait as e:
        sleep(e.x)
app.run()