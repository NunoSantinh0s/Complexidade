import statistics
import matplotlib.pyplot as plt

def complexidade_boxplot(dic_tempos):
    inputs = list(dic_tempos.keys())
    tempos_medios = [statistics.mean(dic_tempos) for dic_tempos in inputs]

    plt.plot(inputs, tempos_medios, marker='o')
    plt.xlabel('Inputs')
    plt.ylabel('Tempo médio de execução')
    plt.show()