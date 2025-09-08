from flask import Flask, render_template, request, redirect, Response, flash
from downloader import audio_downloader, video_downloader
from threading import Thread
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
import os
import queue
import uuid

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

# Stores individual log queues by session/request
log_queues = {}

# Generate timestamped download folder in Downloads directory
def get_download_folder():
    downloads_path = Path.home() / "Downloads"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_path = downloads_path / f"YouTubeDownloads_{timestamp}"
    folder_path.mkdir(parents=True, exist_ok=True)
    return str(folder_path)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        urls = request.form.get("urls")
        mode = request.form.get("mode")

        if not urls or not mode:
            flash("Please enter URLs and select a mode.")
            return redirect("/")

        url_list = [u.strip() for u in urls.strip().splitlines() if u.strip()]
        folder_selected = get_download_folder()

        log_id = str(uuid.uuid4())
        log_queue = queue.Queue()
        log_queues[log_id] = log_queue

        def download_task():
            log_queue.put("🚀 Starting downloads...")
            try:
                if mode == "audio":
                    audio_downloader(url_list, folder_selected, logger=log_queue.put)
                else:
                    video_downloader(url_list, folder_selected, logger=log_queue.put)
                log_queue.put("✅ Download complete!")
                log_queue.put(f"📁 Files saved to: {folder_selected}")
            except Exception as e:
                log_queue.put(f"❌ Error: {str(e)}")
            finally:
                log_queue.put("EOF")

        Thread(target=download_task).start()
        return redirect(f"/progress/{log_id}")

    return render_template("index.html")

@app.route("/progress/<log_id>")
def progress(log_id):
    return render_template("progress.html", log_id=log_id)

@app.route("/logs/<log_id>")
def stream_logs(log_id):
    log_queue = log_queues.get(log_id)
    if not log_queue:
        return Response("Log ID not found", status=404)

    def generate():
        while True:
            message = log_queue.get()
            if message == "EOF":
                break
            yield f"data: {message}\n\n"

        # Cleanup
        del log_queues[log_id]

    return Response(generate(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

