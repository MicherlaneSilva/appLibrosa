import numpy as np 
import matplotlib.pyplot as plt
import librosa
import librosa.display
import pyaudio
import wave
from IPython.display import Audio


def carregarAudio(sound_file):
    return librosa.load(sound_file, sr=44100)


def gerarGrafico(data, fs, sound_file):
    D = librosa.amplitude_to_db(np.abs(librosa.stft(data)))
    librosa.display.specshow(D, x_axis='time', y_axis='linear', sr=fs, cmap='CMRmap')
    plt.title('Espectrograma ' + sound_file)
    plt.xlabel('Tempo [s]')
    plt.ylabel('Frequência [Hz]')
    plt.colorbar(format='%+2.0f dB')
    plt.show()
    
    
def exibirEspectrograma(sound_file):
    data, fs = carregarAudio(sound_file)
    dimensoesGrafico(15, 7)
    gerarGrafico(data, fs, sound_file)
    

def dimensoesGrafico(x, y):
    plt.figure(figsize=(x, y))


def exibirOscilograma(sound_file):
    data, fs = carregarAudio(sound_file)
    dimensoesGrafico(15, 7)
    plt.title('Oscilograma ' + sound_file)
    librosa.display.waveplot(data, fs)
    plt.show()


