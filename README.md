## Telegram Video Downloader Bot

A Telegram bot that allows users to download videos from YouTube and Instagram in `.mp4` format.

### Features

- 📥 **Download Videos**: Supports downloading videos from YouTube and Instagram.
- 📄 **MP4 Format**: Videos are downloaded and sent to users in `.mp4` format.
- 🔗 **Easy to Use**: Just send a video link, and the bot will handle the rest.
- 🗑️ **Auto Cleanup**: Deletes downloaded files after sending them to users.

---

### Installation

Follow these steps to set up and run the bot:

#### Prerequisites
- Python 3.10 or higher installed on your system.
- A valid Telegram bot token from [BotFather](https://core.telegram.org/bots#botfather).

#### Clone the Repository
```bash
git clone https://github.com/imnithishkumar/VideoDownloaderBot.git
cd telegram-video-downloader-bot
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

#### Required Python Libraries
The bot uses the following libraries:
- `python-telegram-bot`: For interacting with the Telegram API.
- `yt-dlp`: For downloading YouTube videos.
- `requests`: For handling HTTP requests.
- `instaloader`: For downloading Instagram videos.

---

### Usage

1. **Set Up the Bot**:
   - Replace `BOT_TOKEN` in the script with your Telegram bot token.

2. **Run the Bot**:
   ```bash
   python bot.py
   ```

3. **Interact with the Bot**:
   - Start the bot in Telegram by sending the `/start` command.
   - Send a YouTube or Instagram video link to download the video.

---

### Directory Structure
```
telegram-video-downloader-bot/
│
├── ShadowMonarch.py     # Main bot script
├── requirements.txt     # Required Python packages
├── README.md            # Project documentation
└── downloads/           # Directory to temporarily store downloaded videos
```

---

### Example Interaction
- **User**: `/start`
- **Bot**: "Welcome to the Video Downloader Bot! 🎥 Send a link to download videos from YouTube or Instagram."
- **User**: `[YouTube/Instagram video link]`
- **Bot**:
  ```
  🔗 Link received! Processing your request...
  📥 Downloading video...
  ✅ Download complete! Sending your file...
  ```

---

### Supported Platforms
- **YouTube**: Download videos in `.mp4` format.
- **Instagram**: Download videos in `.mp4` format.

---

### Notes
- The bot is designed to handle links for YouTube and Instagram only. Support for other platforms can be added in future versions.
- Ensure that the Telegram bot token is kept private to avoid unauthorized access.

---

### Contribution
Feel free to fork this repository and contribute! If you encounter issues or have feature requests, please open an issue or submit a pull request.

---

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Acknowledgements
- [python-telegram-bot](https://python-telegram-bot.org/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [Instaloader](https://instaloader.github.io/)

---

Replace `yourusername` in the repository URL with your GitHub username, and you're good to go! Let me know if you need further customization.
