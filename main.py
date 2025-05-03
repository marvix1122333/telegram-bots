from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)
from flask import Flask
from threading import Thread

# --- Your bot token ---
TOKEN = "7776982345:AAGXHH7LdJf6dLwR9Zafp3jTHbrFabfFO50"

# --- Keep-alive web server setup ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run_web():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    Thread(target=run_web).start()

# --- Bot command handlers ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_text = (
        "📢 *Join Our Trading Signal Channels:*\n"
        "✅ *Get daily 3-6 gold trading signals!*\n"
        "💰 *Stay updated with market trends!*\n"
        "🗂 *Join all channels at once with BEST SIGNAL folder!*\n"
        "🙋‍♂️ *Check MENU to message Admin!*\n\n"
        "🔗 *Click MENU if you need broker's link*"
    )

    folder_invite_link = "https://t.me/addlist/6z8k_Da5huwwM2Y0"  # Replace with your folder invite link

    buttons = [
        [InlineKeyboardButton("📂 Join SIGNALS ONLY Folder", url=folder_invite_link)]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(
        text=message_text,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def masterchannel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("📢 Master Channel: https://t.me/SmcTradingPoin")

async def broker(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("💰 Broker: https://one.exnesstrack.org/a/l1t1rf3p6v")

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("👤 Profile: https://t.me/Mr_Harry99")

# --- Start the bot ---
def main():
    keep_alive()  # Keeps the bot alive via web ping

    app_telegram = Application.builder().token(TOKEN).build()

    app_telegram.add_handler(CommandHandler("start", start))
    app_telegram.add_handler(CommandHandler("masterchannel", masterchannel))
    app_telegram.add_handler(CommandHandler("broker", broker))
    app_telegram.add_handler(CommandHandler("profile", profile))

    print("Bot is running...")
    app_telegram.run_polling()

if __name__ == "__main__":
    main()
