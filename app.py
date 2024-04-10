import base64
import os
from flask import Flask, request, render_template, send_file
import requests
import io

app = Flask(__name__)

def renew_link(url: str) -> str:
    return requests.post("https://discord.com/api/v9/attachments/refresh-urls", json={"attachment_urls": [url]}, headers={"Authorization": "MTIyNDcxNzY4MjM3MzQyNzMwMg.GhgISM.daF5-Dg5UkD0sJqtt3gtXsHrfh_irGoRE_Vwnk", "Content-Type": "application/json", "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"""}).json()["refreshed_urls"][0]["refreshed"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload")
def upload_page():
    return render_template("upload.html")

@app.route("/download")
def download_page():
    return render_template("download.html")

@app.route("/api/download/<path:url>", methods=["GET"])
def download(url):
    try:
        start = request.args.get("start")
        end = str(int(request.args.get("end"))-1)
        headers = {'Range': f'bytes={start}-{end}'}
        if start and end:
            response = requests.get(renew_link(url), headers=headers)
            if response.status_code == 206:
                return response.content
            else:
                return (f"Error: {response.status_code} - {response.reason}")
        else:
            return "Add start/end arguments!"
    except Exception as e:
        return str(e)
