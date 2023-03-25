import queue
import sounddevice as sd
import vosk
import datetime
from vosk import Model, KaldiRecognizer
import json
import words
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import voice


q = queue.Queue()

model = vosk.Model('model_small')

device = sd.default.device  # sd.default.device = 1,3 ////input, output [1, 3]
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])
blocksize = 16000  # Пауза


def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    q.put(bytes(indata))


def main():
    """"Функция для прослушивания микрафона"""
    with sd.RawInputStream(samplerate=samplerate, blocksize=blocksize, device=device[0],
                           dtype="int16", channels=1, callback=callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        query = ""
        while query !='выход':
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                with open('list.txt', 'a') as file:
                    now = datetime.datetime.now()
                    now = now.strftime("%d-%m-%Y %H:%M")
                    file.write(f'{now}:  {data}\n')
                print(data)
            # else:
            #   print(rec.PartialResult())
            query = data



if __name__ == '__main__':
    print('tttt')