import pyaudio
import wave


def gravarAudio(sound_file, tempoDeGravacao):
    chunk = 2048
    formato = pyaudio.paInt32
    canais = 1
    taxaDeAmostragem = 44100
    nomeArquivoSaida = sound_file + ".wav"
 
     
 
    #deltaX= 1.0/taxaDeAmostragem
     
    objetoPyAudio = pyaudio.PyAudio()
     
    streamMic = objetoPyAudio.open(format=formato,channels=canais, rate=taxaDeAmostragem, input=True, frames_per_buffer=chunk)
 
 
 
    framesWav = []
 
    #captura dados do microfone
    for nLoop in range(0, int(taxaDeAmostragem / chunk * tempoDeGravacao)):
        dadosLidosMic = streamMic.read(chunk)
        framesWav.append(dadosLidosMic)
    #framesWav é uma lista com 215 "chunks" de 1024 amostras
 
    streamMic.stop_stream()
    streamMic.close()
    objetoPyAudio.terminate()
     
    #criamos uma única lista com todos os bytes encadeados
    framesWavJuntos= b''.join(framesWav)
 
 
    #salvamos o arquivo wave
    arquivoWav = wave.open(nomeArquivoSaida, 'wb')
    arquivoWav.setnchannels(canais)
    arquivoWav.setsampwidth(objetoPyAudio.get_sample_size(formato))
    arquivoWav.setframerate(taxaDeAmostragem)
    arquivoWav.writeframes(framesWavJuntos)
    arquivoWav.close() 
    
    #return True

