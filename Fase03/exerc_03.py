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
