import time
from pyrogram import Client, filters

@Client.on_message(filters.command("ping"))
async def ping_handler(client, message):
    start_time = time.time()
    response = await message.reply_text("Pinging...")
    end_time = time.time()
    latency = (end_time - start_time) * 1000  # Convert to milliseconds
    await response.edit_text(f"Pong! 🏓\nResponse time: `{int(latency)} ms`")
