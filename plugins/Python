import time
import datetime
BOT_START_TIME = time.time()
from pyrogram import Client, filters
from pyrogram.types import Message

@app.on_message(filters.command("ping") & filters.private)
async def ping_handler(client: Client, message: Message):
    start_time = time.time()
    uptime = str(datetime.timedelta(seconds=int(time.time() - BOT_START_TIME)))
    response = await message.reply("Pinging...")
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000)
    await response.edit(f"**Pong!**\n⏱️ **Uptime:** `{uptime}`\n⚡ **Ping:** `{ping_time}ms`")
