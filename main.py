import pyaudio
import pyautogui as pg
import tkinter as tk
from vosk import Model, KaldiRecognizer

model = Model('vosk-model-small-en-us-0.15')
recog = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

previousText = ''
while True:
    data = stream.read(4096, exception_on_overflow=False)
    if recog.AcceptWaveform(data):
        text = recog.Result()
        text = text[14:-3]
        print(text)
        if text == 'computer open task manager':
            pg.hotkey('ctrl','shift','esc')