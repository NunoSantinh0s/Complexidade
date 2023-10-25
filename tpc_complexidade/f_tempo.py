import time
import statistics

def tempo(funcao, input, n_vezes):
    tempos_execucao = []

    for i in range(n_vezes):
        inicio = time.time()
        resultado = funcao(input)
        fim = time.time()
        tempos_execucao.append(fim - inicio)
    
    tempo_medio = statistics.mean(tempos_execucao)
    desvio_padrao = statistics.stdev(tempos_execucao)

    return tempos_execucao, tempo_medio, desvio_padrao
