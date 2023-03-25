#!/usr/bin/env python3

import queue
import sounddevice as sd
import vosk
from vosk import Model, KaldiRecognizer
import json
import words
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from skills import *
import voice


q = queue.Queue()

model = vosk.Model('model_small')

device = sd.default.device  # sd.default.device = 1,3 ////input, output [1, 3]
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])
blocksize = 16000  # Пауза


def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    q.put(bytes(indata))

def recognize(data, vectorizer, clf):
    trg = words.TRIGGERS.intersection(data.split())
    if not trg:
        return

    data.replace(list(trg)[0], '')
    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]
    # print(answer)

    # получаем имя функции для выполнения
    func_name = answer.split()[0]
    voice.speaker(answer.replace(func_name, ''))
    exec(func_name + '()')  # выполняет нашу распознаную функцию



def main():
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))
    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))

    del words.data_set

    """"Функция для прослушивания микрафона"""
    with sd.RawInputStream(samplerate=samplerate, blocksize=blocksize, device=device[0],
                           dtype="int16", channels=1, callback=callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                recognize(data, vectorizer, clf)
                print(data)
            # else:
            #     print(rec.PartialResult())


if __name__ == '__main__':
    main()


