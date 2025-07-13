# 📞 Instagram Call AudioBot

A Python automation script that monitors Instagram calls and plays a YouTube audio file once a receiver joins. Built using Selenium and `mpv` player with the Brave browser.

---

## 🚀 Features

- Launches an Instagram call using your existing Brave browser session.
- Detects when the other participant joins the call (`+1` indicator).
- Automatically plays a YouTube audio file using `mpv`.
- Easy to configure and customize with your own call link or audio.

---

## 🛠️ Requirements

- Python 3.7+
- [Brave Browser](https://brave.com/)
- [mpv Media Player](https://mpv.io/)
- ChromeDriver compatible with your Brave version
- Selenium for Python

Install dependencies:

```bash
pip install selenium
```
🔧 Configuration
Edit these values in the Python script:

python
Copy
Edit
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
USER_DATA_DIR = r"C:\Users\YourUsername\AppData\Local\BraveSoftware\Brave-Browser\User Data"
CALL_URL = "https://www.instagram.com/call/?has_video=false&ig_thread_id=YOUR_THREAD_ID"
video_url = "https://www.youtube.com/watch?v=qgfQSSnzDLI"
Replace:

YourUsername with your Windows username

YOUR_THREAD_ID with the Instagram call's thread ID

video_url with your preferred YouTube audio

💡 Note: The script assumes you are already logged in to Instagram in the Brave browser.

▶️ Usage
Run the script using Python:

bash
Copy
Edit
python instagram_call_audio.py
The script waits 60 seconds before starting (you can adjust it).

It opens the call URL and clicks the Start call button.

When someone joins the call (+1 detected), it plays your audio file.

🛡️ Disclaimer
This project is intended for educational and automation experimentation purposes only. Make sure to comply with Instagram's terms of service and usage policies when using this script.

📄 License
MIT License. See LICENSE for details.
