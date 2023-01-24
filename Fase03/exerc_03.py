""" 
Olá, este é o um exercício da fase 03.

Crie uma função que recebe um dicionário com os nomes dos alunos reprovados e aprovados em cada matéria.
(exemplo de entrada)
{
    "MATEMÁTICA": {"APROVADOS": [A,B,C], "REPROVADOS": [D,E,F,G,H]},
    "FÍSICA": {"APROVADOS": [A,B,C], "REPROVADOS": [D,E,F,G,H]}, 
    ...
}
Após receber a entrada, retorne um dicionário com as chaves "APROVADOS_EM_TODAS" com os alunos numa tupla ordenada 
alfabeticamente, a chave "REPROVADOS" com uma tupla também ordenada alfabeticamente e por fim uma
chave "DETALHES" com um dicionário que mostra os alunos reprovados ordenados pela quantidade de 
matérias reprovadas. 
(exemplo da chave detalhes)
{
    1: {"nome":[ matérias, reprovadas,...]},
    2: {"nome":[ matérias, reprovadas,...]},
    ...
}

"""

def alunos_apro_repro(materias):
    dicio = {"APROVADOS_EM_TODAS": (), "REPROVADOS": (), "DETALHES": {}}
    list_aprovados = list()
    list_reprovados = list()
    detalhes = dict()
    detalhes2 = dict()

    for mat_, aprov in materias.items():
        list_aprovados.append(set(aprov["APROVADOS"]))
        list_reprovados.append(aprov["REPROVADOS"])

        for det in aprov["REPROVADOS"]:
            if det not in detalhes:
                detalhes[det] = [mat_]
            elif det in detalhes:
                detalhes[det].append(mat_)

    for a in range(1, len(list_aprovados)):
        list_aprovados[0] = list_aprovados[0].intersection(list_aprovados[a])

    for r in list_reprovados:
        list_reprovados[0].extend(r)

    for ordem in sorted(detalhes, key= detalhes.get):
        detalhes2[ordem] = detalhes[ordem]

    dicio['APROVADOS_EM_TODAS'] = tuple(sorted(list_aprovados[0]))
    dicio['REPROVADOS'] = tuple(sorted(set(list_reprovados[0])))
    dicio['DETALHES'] = detalhes2

    return dicio

def main():
    entrada = {
    "MATEMÁTICA": {"APROVADOS": ['A','B','C'], "REPROVADOS": ['D','E','F','G','H']},
    "FÍSICA": {"APROVADOS": ['A','B','C', 'D'], "REPROVADOS": ['E','F','G','H', 'Z']}, 
    "QUIMICA": {"APROVADOS": ['A','B','C', 'D', 'E'], "REPROVADOS": ['F','G','H']}}
    print(alunos_apro_repro(entrada))

if __name__ == '__main__':
    main()