import os
import pyaudio
import pickle
import webbrowser
import AppOpener as ao
import pyautogui as pg
import tkinter as tk
from vosk import Model, KaldiRecognizer


class Command(object):
    def __init__(self, name, keys):
        self.name = name
        self.keys = keys

model = Model('vosk-model-small-en-us-0.15')
recog = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)



computerName = 'computer'
previousText = ''
while True:
    data = stream.read(4096, exception_on_overflow=False)
    if recog.AcceptWaveform(data):
        text = recog.Result()
        text = text[14:-3]
        if computerName + ' task manager' in text:
            pg.hotkey('ctrl','shift','esc')
        if computerName + ' open ' in text:
            text = text[text.index(' open ')+6:len(text)]
            ao.open(text, match_closest=True)
        if computerName + ' close ' in text:
            text = text[text.index(' close ')+7:len(text)]
            ao.close(text)
        if computerName + ' google ' in text:
            text = text[text.index(' google ') + 8:len(text)]
            url = 'www.google.com/search?q='+ text
            webbrowser.open(url)
        if computerName + ' type ' in text:
            print(text)
            text = text[text.index(' type ') + 6:len(text)]
            pg.typewrite(text+' ', interval=0.025)