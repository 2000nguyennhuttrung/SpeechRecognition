import speech_recognition as sr
import pyaudio
from gtts import gTTS
import os
import time
import playsound
import urllib.request
import re

# Khoi tao bo nhan dang
r = sr.Recognizer()


def Speak(text):
    tts = gTTS(text=text, lang='vi')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)


def Listen():
    with sr.Microphone() as mic:
        # print("Mời bạn nói...")
        Speak("Mời bạn nói")
        audio = r.listen(mic)
        try:
            text = r.recognize_google(audio, language="vi-VN")
        except:
            text = ""
    return text


# Tim tren youtube dua vao nhung tu da nhan dang
def Search(keyword):
    keywords = keyword.replace(" ", "+")
    html = urllib.request.urlopen(
        "https://www.youtube.com/results?search_query=" + keywords)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    for i in range(len(video_ids)):
        video_ids[i] = "https://www.youtube.com/watch?v=" + video_ids[i]
    return video_ids


def main():
    text = Listen()
    print(text)

    serach = Search(text)
    for item in serach:
        print(item)


if __name__ == "__main__":
    main()
