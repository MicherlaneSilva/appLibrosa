import os
from multiprocessing import Pool
import test 
import gravarTela

processos = ('test.py', 'gravarTela.py')

def rodar_processo(processo):
    os.system(processo)

pool = Pool(processes=2)
pool.map(rodar_processo, processos)