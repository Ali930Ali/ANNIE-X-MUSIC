from pyrogram import enums
from pyrogram.enums import ChatType
from pyrogram import filters, Client
from ANNIEMUSIC import app
from config import OWNER_ID
from pyrogram.types import Message
from ANNIEMUSIC.utils.jarvis_ban import admin_filter
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton



# ------------------------------------------------------------------------------- #


@app.on_message(filters.command("pin") & admin_filter)
async def pin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("**bu komut yalnızca gruplarda çalışır !**")
    elif not replied:
        await message.reply_text("**Bir mesajı sabitlemek için yanıtla !**")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.pin()
                await message.reply_text(f"**Mesaj başarıyla sabitlendi!**\n\n**sohbet:** {chat_title}\n**yönetici:** {name}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" 📝 Mesajı görüntüler ", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))


@app.on_message(filters.command("pinned"))
async def pinned(_, message):
    chat = await app.get_chat(message.chat.id)
    if not chat.pinned_message:
        return await message.reply_text("**Sabitleşmiş mesaj bulunamadı**")
    try:        
        await message.reply_text("İşte en son sabitleşmiş mesaj",reply_markup=
        InlineKeyboardMarkup([[InlineKeyboardButton(text="📝 Mesajı görüntüler",url=chat.pinned_message.link)]]))  
    except Exception as er:
        await message.reply_text(er)


# ------------------------------------------------------------------------------- #

@app.on_message(filters.command("unpin") & admin_filter)
async def unpin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("**Bu komut sadece gruplarda çalışır !**")
    elif not replied:
        await message.reply_text("**Bir mesaja yanıt vererek sabitlemeyi kaldırın !**")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.unpin()
                await message.reply_text(f"**Başarıyla sabitlemeyi kaldırılan mesaj"!**\n\n**ᴄʜᴀᴛ:** {chat_title}\n**ᴀᴅᴍɪɴ:** {name}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" 📝 ᴠɪᴇᴡs ᴍᴇssᴀɢᴇ ", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))




# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("removephoto") & admin_filter)
async def deletechatphoto(_, message):
      
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("**işleniyor....**")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("**Bu komut gruplarda çalışır !**") 
      try:
         if admin_check.privileges.can_change_info:
             await app.delete_chat_photo(chat_id)
             await msg.edit("**Gruptan profil fotoğrafı başarıyla kaldırıldı !\nʙʏ** {}".format(message.from_user.mention))    
      except:
          await msg.edit("**Kullanıcının grup fotoğrafını kaldırabilmesi için yönetici haklarında değişiklik yapması gerekiyor !**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("setphoto")& admin_filter)
async def setchatphoto(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("İşleniyor...")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("`Bu komut gruplarda çalışır !`") 
      elif not reply:
           await msg.edit("**Bir fotoğrafa veya belgeye yanıt ver.**")
      elif reply:
          try:
             if admin_check.privileges.can_change_info:
                photo = await reply.download()
                await message.chat.set_photo(photo=photo)
                await msg.edit_text("**Yeni profil fotoğrafı başarıyla eklendi !\nʙʏ** {}".format(message.from_user.mention))
             else:
                await msg.edit("**Bir şeyler yanlış gitti, başka bir fotoğraf deneyin !**")
     
          except:
              await msg.edit("**Bir şeyler yanlış gitti, başka bir fotoğraf deneyin !**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("settitle")& admin_filter)
async def setgrouptitle(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("ᴘʀᴏᴄᴇssɪɴɢ...")
    if message.chat.type == enums.ChatType.PRIVATE:
          await msg.edit("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋ ᴏɴ ɢʀᴏᴜᴘs !**")
    elif reply:
          try:
            title = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("**Yeni grup adı başarıyla eklendi !\nʙʏ** {}".format(message.from_user.mention))
          except AttributeError:
                await msg.edit("**Kullanıcının grup başlığını değiştirebilmesi için yönetici haklarını değiştirmesi gerekiyor !**")   
    elif len(message.command) >1:
        try:
            title = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("**Yeni grup adı başarıyla eklendi !\nʙʏ** {}".format(message.from_user.mention))
        except AttributeError:
               await msg.edit("**Kullanıcının grup başlığını değiştirebilmesi için yönetici haklarını değiştirmesi gerekiyor !**")
          

    else:
       await msg.edit("**Grup başlığını değiştirmek için metne yanıt vermeniz veya bir metin sağlamanız gerekiyor **")


# --------------------------------------------------------------------------------- #



@app.on_message(filters.command("setdiscription") & admin_filter)
async def setg_discription(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("**İşleniyor...**")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("**Bu komut gruplar üzerinde çalışır!**")
    elif reply:
        try:
            discription = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("**sᴜᴄᴄᴇssғᴜʟʟʏ ɴᴇᴡ ɢʀᴏᴜᴘ ᴅɪsᴄʀɪᴘᴛɪᴏɴ ɪɴsᴇʀᴛ!**\nʙʏ {}".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("**Kullanıcının grup açıklamasını değiştirebilmesi için yönetici haklarına sahip olması gerekiyor!**")   
    elif len(message.command) > 1:
        try:
            discription = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("**Yeni grup açıklaması başarıyla eklendi!**\nʙʏ {}".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("**Kullanıcının grup açıklamasını değiştirebilmesi için bilgiyi değiştirme yönetici haklarına sahip olması gerekiyor!**")
    else:
        await msg.edit("**Grup açıklamasını değiştirmek için metne yanıt vermeniz veya bir metin sağlamanız gerekiyor!**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("lg")& filters.user(OWNER_ID))
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = "**sᴜᴄᴄᴇssғᴜʟʟʏ ʜɪʀᴏ !!.**"
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)


# --------------------------------------------------------------------------------- #


