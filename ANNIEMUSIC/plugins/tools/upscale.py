import os
import config
from config import BOT_USERNAME
from ANNIEMUSIC import app
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import aiofiles
import aiohttp
import requests

async def load_image(image_path: str, url: str) -> str:
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                async with aiofiles.open(image_path, mode="wb") as file:
                    await file.write(await response.read())
                return image_path
            return None

@app.on_message(filters.command("upscale", prefixes="/"))
async def upscale_image(client, message):
    chat_id = message.chat.id
    replied_message = message.reply_to_message
    
    if not config.DEEP_API:
        return await message.reply_text("Deep API anahtarı olmadan ölçeklendiremem!")
    
    if not replied_message or not replied_message.photo:
        return await message.reply_text("Lütfen bir resme cevap verin.")
    
    aux_message = await message.reply_text("Ölçeklendirme yapılıyor, lütfen bekleyin...")
    image_path = await replied_message.download()
    
    response = requests.post(
        "https://api.deepai.org/api/torch-srgan",
        files={'image': open(image_path, 'rb')},
        headers={'api-key': config.DEEP_API}
    ).json()
    
    image_url = response.get("output_url")
    if not image_url:
        return await aux_message.edit("Resmi ölçeklendirmekte başarısız oldum, lütfen tekrar deneyin.")
    
    downloaded_image = await load_image(image_path, image_url)
    if not downloaded_image:
        return await aux_message.edit("Ölçeklendirilmiş resmi indirmekte başarısız oldum, lütfen tekrar deneyin.")
    
    await aux_message.delete()
    await message.reply_photo(photo=downloaded_image)

@app.on_message(filters.command("getdraw", prefixes="/"))
async def draw_image(client, message):
    chat_id = message.chat.id
    user_id = message.sender_chat.id if message.sender_chat else message.from_user.id
    replied_message = message.reply_to_message
    
    if not config.DEEP_API:
        return await message.reply_text("Deep API anahtarı olmadan görüntü oluşturamam!")
    
    if replied_message and replied_message.text:
        query = replied_message.text
    elif len(message.text.split()) > 1:
        query = message.text.split(None, 1)[1]
    else:
        return await message.reply_text("lütfen metin sağlayın veya kısa mesaja yanıt verin.")
    
    aux_message = await message.reply_text("Resim oluşturuluyor, lütfen bekleyin...")
    image_path = f"cache/{user_id}_{chat_id}_{message.id}.png"
    
    response = requests.post(
        "https://api.deepai.org/api/text2img",
        data={'text': query, 'grid_size': '1', 'image_generator_version': 'hd'},
        headers={'api-key': config.DEEP_API}
    ).json()
    
    image_url = response.get("output_url")
    if not image_url:
        return await aux_message.edit("Resim oluşturulamadı, lütfen tekrar deneyin.")
    
    downloaded_image = await load_image(image_path, image_url)
    if not downloaded_image:
        return await aux_message.edit("Oluşturulan görsel indirilemedi, lütfen deneyin.")
    
    await aux_message.delete()
    await message.reply_photo(photo=downloaded_image, caption=query)
