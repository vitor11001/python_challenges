""" 
Olá, este é o um exercício da fase 03. 

Crie as funções a seguir:
    - Crie uma função que recebe uma lista de idades e retorna, numa tupla, somente a maior idade.
    - Crie uma função que recebe uma lista de idades e retorna um dicionário com as chaves "MAIOR_IDADE" E "MENOR_IDADE".
    - Crie uma função que recebe uma lista de idades e retorna uma tupla com as idade ordenadas de maneira crescente.
"""

def maior_idade_lista(idades):
    idades = sorted(idades)
    return (idades[-1], )

def idades_maior_menor_dicionario(idades):
    idades = sorted(idades)
    return {'MAIOR_IDADE': idades[-1], 'MENOR_IDADE': idades[0]}
    
def idades_tupla(idades):
    return tuple(sorted(idades))

def main():
    idades = [15,14,6,2,5,8,19,12,32,64,90,10,100,20]
    print(f'Maior idade: {maior_idade_lista(idades)} Type: {type(maior_idade_lista(idades))}')
    print(idades_maior_menor_dicionario(idades))
    print(idades_tupla(idades))

if __name__ == '__main__':
    main()