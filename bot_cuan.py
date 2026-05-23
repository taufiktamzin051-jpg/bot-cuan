import re
import os
from telethon import TelegramClient, events

# --- KONFIGURASI ---
# Ganti dengan data asli lu dari my.telegram.org
api_id =  34236158
api_hash = 8f93fe2bb72ee6b76d8cf7893b62c4be

# Link Involve Asia lu (contoh: https://invol.co/clABCDE?url=)
BASE_AFF_LINK = "https://invl.io/clnh1yd?url=." 

# Username channel (Gunakan '@' atau username tanpa @)
CHANNEL_SUMBER =(https://t.me/racun_shopee_murah_promo_diskon)
(https://t.me/Racun_Shopee_Murah_Diskon_Receh)
CHANNEL_TUJUAN = 'https://t.me/gudangsolusihemat'

# Nama session
client = TelegramClient('session_cuan', api_id, api_hash)

# --- FUNGSI UTAMA ---
def convert_link(text):
    # Regex untuk mencari link shopee.co.id
    shopee_pattern = r'(https?://shopee\.co\.id/\S+)'
    
    def replace_with_affiliate(match):
        original_url = match.group(0)
        return BASE_AFF_LINK + original_url

    return re.sub(shopee_pattern, replace_with_affiliate, text)

@client.on(events.NewMessage(chats=CHANNEL_SUMBER))
async def handler(event):
    if event.message.text:
        text_baru = convert_link(event.message.text)
        await client.send_message(CHANNEL_TUJUAN, text_baru, file=event.message.media)
        print("Pesan berhasil di-forward!")

print("Bot Cuan Sedang Berjalan...")
client.start()
client.run_until_disconnected()
