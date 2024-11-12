import os
from flask import Flask, flash, render_template, redirect, request
import sys 
import time
import datetime
import os
import uuid
import pandas as pd
import sys
import scrapetube
import csv
import gc
import yt_dlp
import requests
import time

app = Flask(__name__)

def get_youtube_transcript(video_url):
    ydl_opts = {'quiet':True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        transcript = info.get('automatic_captions', {}).get('en', None)
        if transcript:
            return transcript[-1]['url']
        else:
            return "Transcript not available for this video."
        

@app.route('/')
def main():
    return {"hello": "hi"}

@app.route('/transcribe', methods=['GET'])
def saver():
    time_init = time.time()
    video_id = request.url.split("?")[-1]

    transcript = get_youtube_transcript(video_id)
    return {"transcript": transcript, "time_taken": str(time.time()-time_init)}