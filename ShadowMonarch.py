import asyncio
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update
import yt_dlp
import requests
import os
import instaloader

BOT_TOKEN = "7325845075:AAFPuUFgZg6nwS8nUqqMbSRK-sChsRIxsDc"
DOWNLOAD_DIR = "downloads"

# Ensure the downloads directory exists
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to the Video Downloader Bot! 🎥\n\nSend a link to download videos from YouTube or Instagram."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    chat_id = update.message.chat_id

    await update.message.reply_text("🔗 Link received! Processing your request...")
    try:
        if "youtube.com" in user_message or "youtu.be" in user_message:
            await update.message.reply_text("📥 Downloading YouTube video...")
            file_path = download_youtube(user_message, DOWNLOAD_DIR)
        elif "instagram.com" in user_message:
            await update.message.reply_text("📥 Downloading Instagram video...")
            file_path = download_instagram(user_message, DOWNLOAD_DIR)
        else:
            await update.message.reply_text(
                "❌ Unsupported link! Currently, this bot supports YouTube and Instagram links. More platforms coming soon!"
            )
            return

        await update.message.reply_text("✅ Download complete! Sending your file...")
        # Send the downloaded file as a document
        await context.bot.send_document(chat_id=chat_id, document=open(file_path, "rb"))
        os.remove(file_path)  # Clean up the file after sending
    except Exception as e:
        await update.message.reply_text(f"⚠️ Failed to process the link: {str(e)}")

def download_youtube(url, output_dir):
    ydl_opts = {
        'outtmpl': f"{output_dir}/%(title)s.%(ext)s",
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # Ensure .mp4 format
        'merge_output_format': 'mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)

def download_instagram(url, output_dir):
    loader = instaloader.Instaloader(download_pictures=False, save_metadata=False, download_videos=True)
    post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])
    video_url = post.video_url
    response = requests.get(video_url)
    file_path = os.path.join(output_dir, f"{post.shortcode}.mp4")
    with open(file_path, "wb") as f:
        f.write(response.content)
    return file_path

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot using the already running event loop
    loop = asyncio.get_event_loop()
    loop.create_task(application.run_polling())

if __name__ == "__main__":
    main()
