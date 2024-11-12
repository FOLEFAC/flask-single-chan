import os
from flask import Flask, flash, render_template, redirect, request
import sys 
import time
from youtube_transcript_api import YouTubeTranscriptApi
import datetime
import uuid
import pandas as pd
import scrapetube
import csv
import gc

langs = ["ab", "aa", "af", "ak", "sq", "am", "ar", "hy", "as", "ay", "az", "bn", "ba", "eu", "be", "bho", "bs", "br", "bg", "my", "ca", "ceb", "zh-Hans", "zh-Hant",
         "co", "hr", "cs", "da", "dv", "nl", "dz", "en", "eo", "et", "ee", "fo", "fj", "fil", "fi", "fr", "gaa", "gl", "lg", "ka", "de", "el", "gn", "gu", "ht",
         "ha", "haw", "iw", "hi", "hmn", "hu", "is", "ig", "id", "ga", "it", "ja", "jv", "kl", "kn", "kk", "kha", "km", "rw", "ko", "kri", "ku", "ky", "lo", "la",
         "lv", "ln", "lt", "luo", "lb", "mk", "mg", "ms", "ml", "mt", "gv", "mi", "mr", "mn", "mfe", "ne", "new", "nso", "no", "ny", "oc", "or", "om", "os", "pam",
         "ps", "fa", "pl", "pt", "pt-PT", "pa", "qu", "ro", "rn", "ru", "sm", "sg", "sa", "gd", "sr", "crs", "sn", "sd", "si", "sk", "sl", "so", "st", "es",
         "su", "sw", "ss", "sv", "tg", "ta", "tt", "te", "th", "bo", "ti", "to", "ts", "tn", "tum", "tr", "tk", "uk", "ur", "ug", "uz", "ve", "vi", "war", "cy",
         "fy", "wo", "xh", "yi", "yo", "zu", "en-IN", "en-US"]

def break_into_chunks(text, chunk_size=500):
    chunks = []
    num_chunks = len(text.split(" "))//500
    for i in range(num_chunks):

        chunks.append(' '.join(text.split(" ")[chunk_size*i:chunk_size*(i+1)]))

    return chunks

app = Flask(__name__)

@app.route('/')
def main():
    return {"hello": "hi"}

# @app.post("/create_user/")
# async def create_user(user_data: UserCreate):
#     user_id = user_data.user_id
#     username = user_data.username
#     return {
#         "msg": "we got data succesfully",
#         "user_id": user_id,
#         "username": username,
#     }

@app.route('/transcribe', methods=['GET'])
def transcription():
    #print("okkkkkkkkkkkk")
    info = request.url.split("?")
    video_id = info[1]
    
    time_init = time.time()
    data_video = []
    try:
        yt = YouTubeTranscriptApi.get_transcript(video_id[:11], languages=langs, proxies={"https": "127.0.0.1:8000"})

    except Exception as error:
        #print("--An error occurred:", type(error).__name__, error)
        print("no subtitle"+"-"+video_id)
        return {"data_videos": [{'video_id':video_id, 'position':0, 'transcript':""}]}
    #print("time_1", str(time.time()-time_init)+""+video_id)
    transcript = ''
    for i,t in enumerate(yt):
        transcript+=' '+t['text']
    chunks = break_into_chunks(transcript.replace("\n"," "), 499)
    try:
        if len(chunks)==0:
            data_video.append({'video_id':video_id, 'position':0, 'transcript':transcript})
        else:
            for pos, chunk in enumerate(chunks):
                try:
                    if pos==len(chunks)-1:
                        data_video.append({'video_id':video_id, 'position':pos, 'transcript':chunk})
                    else:
                        data_video.append({'video_id':video_id, 'position':pos, 'transcript':chunk})
                    
                except Exception as error:
                    pass
    except Exception as error:
        print("--An error occurred:", type(error).__name__, "–"+video_id, error)
        return {"data_videos": data_video}
    
    #print("time-->", str(time.time()-time_init)+""+video_id)
    return {"data_videos": data_video}