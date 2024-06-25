import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# Telegram API credentials - Get these from the Telegram API website
API_ID = int(getenv("24685579"))
API_HASH = getenv("0c59512c1c2437c5f305cba1d47c07c5")
BOT_TOKEN = getenv("7476130132:AAFt9OMZbMP9vOQ10qcp6SxNKS5aQd7fbD4")

# Specify where to get the following credentials
OWNER_USERNAME = getenv("OWNER_USERNAME", "debubluman")
BOT_USERNAME = getenv("BOT_USERNAME", "EsilaChatBot")
BOT_NAME = getenv("BOT_NAME", "˹𝐄𝐬𝐢𝐥𝐚 𝐬𝐨𝐡𝐛𝐞𝐭˼ ♪")
ASSUSERNAME = getenv("ASSUSERNAME", "esilamuzikasistan")
EVALOP = list(map(int, getenv("EVALOP", "6797202080").split()))
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
LOGGER_ID = int(getenv("LOGGER_ID", -1002014167331))
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# External APIs - Get these from their respective providers
GPT_API = getenv("GPT_API")
DEEP_API = getenv("DEEP_API")
OWNER_ID = int(getenv("OWNER_ID", debubluman))

# Heroku deployment settings - Refer to Heroku documentation on how to obtain these
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Ali930Ali/ANNIE-X-MUSIC")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support and contact information - Provide your own support channels
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/esilabotbilgilendirme")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/sorundestekk")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Server limits and configurations - These can be set based on your server configurations
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

# External service credentials - Obtain these from Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

# Telegram file size limits - Set these according to your requirements
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# Pyrogram session strings - You need to generate these yourself
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Bot introduction messages - These can be customized as per your preference
AYU = [
    "💞", "🦋", "🔍", "🧪", "🦋", "⚡️", "🔥", "🦋", "🎩", "🌈", "🍷", "🥂", "🦋", "🥃", "🥤", "🕊️",
    "🦋", "🦋", "🕊️", "🦋", "🕊️", "🦋", "🦋", "🦋", "🪄", "💌", "🦋", "🦋", "🧨"
]

AYUV = [
    "Merhaba {0}, 🥀\n\n Bu ben {1} !\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ Desteklenen platformlar: ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Çalışma süresi: : {2}\n┠ ➥ Sunucu Depolama : {3}\n┠ ➥ CPU Yükü : {4}\n┠ ➥ RAM Tüketim : {5}\n┠ ➥ ᴜꜱᴇʀꜱ : {6}\n┠ ➥ Sohbetler : {7}\n┗━━━━━━━━━━━━━━━━━⧫\n\n🫧 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🪽 ➪ [Emir💗](https://t.me/debubluman)",
    "Merhaba, {0} ~\n\n◆ Ben  {1} Telegram akış botu bazı faydalı\n◆ ◆ Ultra hızlı VC oynatıcı özellikleri.\n\n✨ Özellikler ⚡️\n◆ ◆ Telegram grupları için bot.\n◆ ◆ Süper hızlı, gecikmesiz oynatıcı\n◆ ◆ Müzik ve video oynatabilirsiniz.\n◆ ◆ Canlı yayın.\n◆ Esila ile yaşam tarzı\n◆ ◆ En iyi ses kalitesi.\n◆ 24×7 ◆müzik çalabilirsiniz..\n◆ ◆ Bu botu grubunuza ekleyin, yönetici yapın ve müziğin tadını çıkarın 🎵..\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ Desteklenen Platformlar : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Çalışma süresi: {2}\n┠ ➥ Sunucu Depolama : {3}\n┠ ➥ CPU Yükü :{4}\n┠ ➥ RAM Tüketimi : {5}\n┠ ➥ Kullanıcılar : {6}\n┠ ➥ Gruplar :{7}\n┗━━━━━━━━━━━━━━━━━⧫\n\n🫧 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🪽 ➪ [Emir💗](https://t.me/Debubluman)",
    "Selam {0}, 🥀\n\n Bu Ben {1} !\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ Desteklenen platformlar: ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Çalışma süresi: : {2}\n┠ ➥ Sunucu Depolama : {3}\n┠ ➥ CPU Yükü : {4}\n┠ ➥ RAM Tüketim : {5}\n┠ ➥ ᴜꜱᴇʀꜱ : {6}\n┠ ➥ Sohbetler :{7}\n┗━━━━━━━━━━━━━━━━━⧫\n\n🫧 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🪽 ➪ [Emir💗](https://t.me/debubluman)",
   "Merhaba, {0} ~\n\n◆ Ben  {1} Telegram akış botu bazı faydalı\n◆ ◆ Ultra hızlı VC oynatıcı özellikleri.\n\n✨ Özellikler ⚡️\n◆ ◆ Telegram grupları için bot.\n◆ ◆ Süper hızlı, gecikmesiz oynatıcı\n◆ ◆ Müzik ve video oynatabilirsiniz.\n◆ ◆ Canlı yayın.\n◆ Esila ile yaşam tarzı\n◆ ◆ En iyi ses kalitesi.\n◆ 24×7 ◆müzik çalabilirsiniz..\n◆ ◆ Bu botu grubunuza ekleyin, yönetici yapın ve müziğin tadını çıkarın 🎵..\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ Desteklenen Platformlar : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Çalışma süresi: {2}\n┠ ➥ Sunucu Depolama : {3}\n┠ ➥ CPU Yükü :{4}\n┠ ➥ RAM Tüketimi : {5}\n┠ ➥ Kullanıcılar : {6}\n┠ ➥ Gruplar :{7}\n┗━━━━━━━━━━━━━━━━━⧫\n\n🫧 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🪽 ➪ [Emir💗](https://t.me/debubluman)",
     "Merhaba {0}, 🥀\n\n Bu ben {1} !\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ Desteklenen platformlar: ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Çalışma süresi: : {2}\n┠ ➥ Sunucu Depolama : {3}\n┠ ➥ CPU Yükü : {4}\n┠ ➥ RAM Tüketim : {5}\n┠ ➥ ᴜꜱᴇʀꜱ : {6}\n┠ ➥ Sohbetler : {7}\n┗━━━━━━━━━━━━━━━━━⧫\n\n🫧ᴅᴇᴠᴇʟᴏᴩᴇʀ 🪽 ➪ [Emir💗](https://t.me/Debubluman)"
]

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
)
PING_VID_URL = getenv(
    "PING_VID_URL", "https://telegra.ph/file/4be43ed2aa6872337e9a8.mp4"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/94e9eca3b0ec6e2dc6cd5.png"
STATS_VID_URL = "https://telegra.ph/file/e2ab6106ace2e95862372.mp4"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/ef5bdba78c475a9e50d24.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/c8db17e1612487be13571.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/6a81d918bd5d44c646205.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/1470316a51382cc446fe1.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/06679f04da4b2fbbb12d0.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/06679f04da4b2fbbb12d0.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/06679f04da4b2fbbb12d0.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/06679f04da4b2fbbb12d0.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - SUPPORT_CHANNEL URL'niz yanlış. Lütfen şununla başladığından emin olun: https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - SUPPORT_CHAT URL'niz yanlış. Lütfen şununla başladığından emin olun: https://"
)
