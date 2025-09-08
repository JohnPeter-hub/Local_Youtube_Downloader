# Local_Youtube_Downloader
Download YouTube videos or audio via a clean Flask web app — Dockerized and ready to run.

# 🎬 YouTube Downloader Web App (Dockerized)

A simple, elegant Flask web app to download YouTube videos or audio — with a responsive Bootstrap UI, real-time download logs, and fully Dockerized deployment.

---

## 🚀 Quick Start with Docker (Recommended)

No Python installation needed. Just clone, build, and run:

# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/youtube-downloader.git
cd youtube-downloader

# 2. Build the Docker image
docker build -t youtube-downloader .

# 3. Run the container on port 5050
docker run -p 5050:5000 youtube-downloader

🔗 Open your browser and go to: http://localhost:5050
💡 Tip: If port 5050 is in use, change it as needed (e.g., -p 8080:5000)

✨ Features
🎯 Download multiple YouTube URLs
🎵 Choose Audio (MP3) or Video (MP4)
⚡ Real-time progress with live logging
📱 Mobile-friendly UI using Bootstrap 5
🐳 Easy setup using Docker


🧪 (Optional) Run Locally Without Docker
If you'd rather run it natively with Python:
# 1. Set up a virtual environment
python -m venv venv
source venv/bin/activate       
(On Windows: venv\Scripts\activate)

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the Flask app
python app.py


⚠️ Disclaimer

This tool is intended for educational purposes only.
Please download videos only if you have the rights or permission to do so.
Respect copyright laws and content creators.

Created by 🦉 for AVRI1
