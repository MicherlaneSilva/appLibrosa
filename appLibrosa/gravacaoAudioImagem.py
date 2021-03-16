from test import gravarAudio
from gravarTela import gravar
import multiprocessing


def gravacao(sound_file, tempo):
    p1 = multiprocessing.Process(target=gravarAudio, args=(sound_file, tempo))
    p2 = multiprocessing.Process(target=gravar, args=(tempo, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    return True



