#!/usr/bin/env python3
from scipy.io import wavfile as wav
import pyaudio
import wave
import numpy as np

FORMAT = pyaudio.paInt16  # format of sampling 16 bit int
CHANNELS = 1  # number of channels it means number of sample in every sampling
RATE = 44100  # number of sample in 1 second sampling
CHUNK = 1024  # length of every chunk
RECORD_SECONDS = 1  # time of recording in seconds
WAVE_OUTPUT_FILENAME = "file.wav"  # file name

while True :
    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("recording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("finished recording")

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # storing voice
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    # reading voice
    rate, data = wav.read('file.wav')

    fftList = np.fft.fft(data)
    half_fftList = []
    for item in range(0, int(len(fftList) / 2)):
        half_fftList.append(abs(fftList[item]))

    average = sum(half_fftList) / float(len(half_fftList))

    access = False
    # keys: 1 4 7 *
    for i in range(1200, 1215):
        if half_fftList[i] >= 20 * average:
            for j in range(693, 703):
                if half_fftList[j] >= 20 * average:
                    print("1")
                    access = True
                    break
            if access == True:
                break

            for j in range(765, 775):
                if half_fftList[j] >= 20 * average:
                    print("4")
                    access = True
                    break
            if access == True:
                break

            for j in range(847, 857):
                if half_fftList[j] >= 20 * average:
                    print("7")
                    access = True
                    break
            if access == True:
                break

            for j in range(936, 946):
                if half_fftList[j] >= 20 * average:
                    print("*")
                    access = True
                    break
            if access == True:
                break

        if access == True:
            break

    if access == True:
        continue

    # keys: 2 5 8 0
    for i in range(1330, 1341):
        if half_fftList[i] >= 20 * average:
            for j in range(693, 703):
                if half_fftList[j] >= 20 * average:
                    print("2")
                    access = True
                    break

            if access == True:
                break

            for j in range(765, 775):
                if half_fftList[j] >= 20 * average:
                    print("5")
                    access = True
                    break
            if access == True:
                break

            for j in range(847, 857):
                if half_fftList[j] >= 20 * average:
                    print("8")
                    access = True
                    break

            if access == True:
                break
            for j in range(936, 946):
                if half_fftList[j] >= 20 * average:
                    print("0")
                    access = True
                    break
            if access == True:
                break
        if access == True:
            break

    if access == True:
        continue

    # keys: 3 6 9 #
    for i in range(1472, 1483):
        if half_fftList[i] >= 20 * average:
            for j in range(693, 703):
                if half_fftList[j] >= 10 * average:
                    print("3")
                    access = True
                    break

            if access == True:
                break

            for j in range(765, 775):
                if half_fftList[j] >= 20 * average:
                    print("6")
                    access = True
                    break
            if access == True:
                break

            for j in range(847, 857):
                if (half_fftList[j] >= 20 * average):
                    print("9")
                    access = True
                    break

            if access == True:
                break
            for j in range(936, 946):
                if half_fftList[j] >= 20 * average:
                    print("#")
                    access = True
                    break
            if access == True:
                break
        if access == True:
            break
    if access == True:
        continue

    # keys: A B C D
    for i in range(1627, 1638):
        if half_fftList[i] >= 20 * average:
            for j in range(693, 703):
                if half_fftList[j] >= 20 * average:
                    print("A")
                    access = True
                    break

            if access == True:
                break

            for j in range(765, 775):
                if half_fftList[j] >= 20 * average:
                    print("B‌‌")
                    access = True
                    break
            if access == True:
                break

            for j in range(847, 857):
                if half_fftList[j] >= 20 * average:
                    print("C")
                    access = True
                    break

            if access == True:
                break
            for j in range(936, 946):
                if half_fftList[j] >= 20 * average:
                    print("D")
                    access = True
                    break
            if access == True:
                break
        if access == True:
            break
         print("A")
