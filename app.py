import base64
import os
from flask import Flask, request, render_template, send_file
from api.webhook import Webhook
from api import cdn
import io

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload")
def upload_page():
    return render_template("upload.html")

@app.route("/download")
def download_page():
    return render_template("download.html")
