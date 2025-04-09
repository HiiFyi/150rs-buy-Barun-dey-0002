from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
import time

def ping(update: Update, context: CallbackContext) -> None:
    start = time.time()
    message = update.message.reply_text("Pinging...")
    end = time.time()
    ping_time = (end - start) * 1000
    context.bot.edit_message_text(
        chat_id=message.chat_id,
        message_id=message.message_id,
        text=f"Pong! `{int(ping_time)}ms`",
        parse_mode="Markdown"
    )

# Add the handler to your dispatcher
dispatcher.add_handler(CommandHandler("ping", ping))
