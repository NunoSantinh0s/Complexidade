from tpc_complexidade import f_tempo


def complexidade(funcao, lista_input, n_vezes):
    dic_stats = {}
    dic_tempos = {}

    for input in lista_input:
        tempos_execucao, tempo_medio, desvio_padrao = f_tempo(funcao, input, n_vezes)
        dic_stats[input] = (tempo_medio, desvio_padrao)
        dic_tempos[input] = tempos_execucao

    return dic_stats, dic_tempos