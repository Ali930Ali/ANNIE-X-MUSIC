from pyrogram import filters
from pyrogram.types import Message
from ANNIEMUSIC.plugins.tools.pretenderdb import impo_off, impo_on, check_pretender, add_userdata, get_userdata, usr_data
from ANNIEMUSIC import app




@app.on_message(filters.group & ~filters.bot & ~filters.via_bot, group=69)
async def chk_usr(_, message: Message):
    if message.sender_chat or not await check_pretender(message.chat.id):
        return
    if not await usr_data(message.from_user.id):
        return await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    usernamebefore, first_name, lastname_before = await get_userdata(message.from_user.id)
    msg = ""
    if (
        usernamebefore != message.from_user.username
        or first_name != message.from_user.first_name
        or lastname_before != message.from_user.last_name
    ):
        msg += f"""
**🔓 Sahte tespit edildi 🔓**
➖➖➖➖➖➖➖➖➖➖➖➖
**🍊 isim** : {message.from_user.mention}
**🍅 Kullanıcı Kimliği** : {message.from_user.id}
➖➖➖➖➖➖➖➖➖➖➖➖\n
"""
    if usernamebefore != message.from_user.username:
        usernamebefore = f"@{usernamebefore}" if usernamebefore else "KULLANICI ADI YOK"
        usernameafter = (
            f"@{message.from_user.username}"
            if message.from_user.username
            else "NO USERNAME"
        )
        msg += """
**🐻‍❄️ Kullanıcı adı değiştirildi 🐻‍❄️**
➖➖➖➖➖➖➖➖➖➖➖➖
**🎭 dan** : {bef}
**🍜 a** : {aft}
➖➖➖➖➖➖➖➖➖➖➖➖\n
""".format(bef=usernamebefore, aft=usernameafter)
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if first_name != message.from_user.first_name:
        msg += """
**🪧 İlk adı değiştirir 🪧**
➖➖➖➖➖➖➖➖➖➖➖➖
**🔐 dan** : {bef}
**🍓 e** : {aft}
➖➖➖➖➖➖➖➖➖➖➖➖\n
""".format(
            bef=first_name, aft=message.from_user.first_name
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if lastname_before != message.from_user.last_name:
        lastname_before = lastname_before or "NO LAST NAME"
        lastname_after = message.from_user.last_name or "NO LAST NAME"
        msg += """
**🪧 Soyadı değiştirir 🪧**
➖➖➖➖➖➖➖➖➖➖➖➖
**🚏dan** : {bef}
**🍕 a** : {aft}
➖➖➖➖➖➖➖➖➖➖➖➖\n
""".format(
            bef=lastname_before, aft=lastname_after
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if msg != "":
        await message.reply_photo("https://telegra.ph/file/d4ad9d539f6297cc5f7a2.jpg", caption=msg)


@app.on_message(filters.group & filters.command("imposter") & ~filters.bot & ~filters.via_bot)
async def set_mataa(_, message: Message):
    if len(message.command) == 1:
        return await message.reply("**Sahte kullanıcıların kullanımını tespit et : sahtekar ᴏɴ|ᴏғғ**")
    if message.command[1] == "enable":
        cekset = await impo_on(message.chat.id)
        if cekset:
            await message.reply("**Sahtekar modu zaten etkin.**")
        else:
            await impo_on(message.chat.id)
            await message.reply(f"**Sahtekar modu başarıyla etkinleştirildi** {message.chat.title}")
    elif message.command[1] == "disable":
        cekset = await impo_off(message.chat.id)
        if not cekset:
            await message.reply("**Sahtekar modu zaten devre dışı.**")
        else:
            await impo_off(message.chat.id)
            await message.reply(f"**Sahtekar modu başarıyla devre dışı bırakıldı** {message.chat.title}")
    else:
        await message.reply("**Sahte kullanıcıları tespit etme kullanımı : sahtekar ᴏɴ|ᴏғғ**")
