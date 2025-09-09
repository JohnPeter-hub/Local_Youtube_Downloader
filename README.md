# 🎬 YouTube Downloader Web App (Dockerized)

A simple, elegant Flask web app to download YouTube videos or audio — with a responsive Bootstrap UI, real-time download logs, and fully Dockerized deployment.

## ✨ Features

### 🎯 Download multiple YouTube URLs

### 🎵 Choose Audio (MP3) or Video (MP4)

### ⚡  Real-time progress with live logging

### 🔐 Safe and private — runs entirely on your machine, not the web.

### 🐳 Easy setup with Docker support

---

# 🚀 How to Run the App
You have three ways to get started. The easiest is pulling the Docker image from Docker Hub — no need to clone or install anything and the app will run in your localhost.

## 🟢 Option 1: Run via Docker Hub (Recommended – just 1 Command)
✅ No setup, no cloning — just pull and run. Copy the below command in your terminal. Make sure you have Docker CLI installed.

<mark>docker run -p 8000:5000 itsyoh/local-youtube-downloader</mark><br>
🔗 Open your browser: http://localhost:8000<br>
💡 If port 8000 is in use, change it as needed (e.g., -p 8080:5000)<br>


## 🐳 Option 2: Clone Repo + Run with Docker
🔧Useful if you want to tweak the code or rebuild the image locally.
### 1. Clone the repo
<mark>git clone https://github.com/JohnPeter-hub/Local_Youtube_Downloader.git</mark><br>
cd Local_Youtube_Downloader

### 2. Build the Docker image
<mark>docker build -t youtube-downloader .</mark>

### 3. Run the container
<mark>docker run -p 8000:5000 youtube-downloader</mark><br>
🔗 Open your browser: http://localhost:8000<br>
💡 If port 8000 is in use, change it as needed (e.g., -p 8080:5000)<br>

## 🧪 Option 3: Run Locally with Python (No Docker)
💻For developers who prefer running the Flask app directly.
### 1. Clone the repo
<mark>git clone https://github.com/JohnPeter-hub/Local_Youtube_Downloader.git</mark><br>
<mark>cd Local_Youtube_Downloader</mark>

### 2. Set up virtual environment
<mark>python -m venv venv</mark><br>
<mark>source venv/bin/activate</mark><br>
<mark>(On Windows: venv\Scripts\activate)</mark>

### 3. Install dependencies
<mark>pip install -r requirements.txt</mark>

### 4. Run the Flask app
<mark>python app.py</mark>

## Walkthrough
**1.Enter URL(s) in the text area. For multiple URLs, separate them into new lines. List can include single videos, multiple videos, single playlist, multiple playlist or all together**<br>
**2.Select either Audio or Video from the radio buttons. Audio will download the file in .mp3 format and Video in .mp4(highest available quality)**<br>
<img width="2858" height="1610" alt="image" src="https://github.com/user-attachments/assets/03ab0c30-d99c-4773-8bd4-7db4d630ce71" /><br>
**3.Click on the Download button. The download begins.**<br>
<img width="2858" height="1610" alt="image" src="https://github.com/user-attachments/assets/8d95ed62-dee5-4aa0-9161-798847cc6fe2" /><br>
**4.Once the download is completed, you'll be able to view the files in the mentioned folder.**




<br>

## ⚠️ Disclaimer

This tool is intended for personal usage only.<br>
Please download videos only if you have the rights or permission to do so.<br>
Respect copyright laws and content creators.<br>

**Created by 🦉 for AVRI1<br>
GitHub: @JohnPeter-hub**
