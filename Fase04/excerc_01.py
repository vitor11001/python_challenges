"""
Olá, este é o um exercício da fase 04. 

Exercícios: 
    Crie um programa que abre um arquivo A, somente se este existir, e 
    escrever 'Senfio' no fim do arquivo. O mesmo programa deve abrir 
    um arquivo B, e criá-lo caso não exista, e escrever 'Senfio'. 
    Trate todos os erros.

"""

class Fase_4():
    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self.senfio = 'Senfio'
        
    def confere_existencia(self):
        try:
            with open(self.arquivo, 'r') as arq:
                return True
            
        except FileNotFoundError:
            print(f'Erro, arquivo não encontrado, confira o diretorio: {self.arquivo}')
            return False
            
    def abre_arquivo_adiciona(self):
        try:
            with open(self.arquivo, 'a') as arq:
                print(f'Arquivo aberto! {self.arquivo}')
                arq.write('\n' + self.senfio)
        
        except FileNotFoundError:
            print(f'Erro, arquivo não encontrado, confira o diretorio: {self.arquivo}')

    def abre_cria_edita_arquivo(self):
        try:
            with open(self.arquivo, 'w+') as arq:
                print(f'Arquivo aberto! {self.arquivo}')
                arq.write(self.senfio)
        
        except FileNotFoundError:
            print(f'Erro, arquivo não encontrado, confira o diretorio: {self.arquivo}')
            
            
def main():
    path_arquivo_A = "./Fase04/arquivo_A.txt"
    path_arquivo_B = "./Fase04/arquivo_B.txt"
    
    if Fase_4(path_arquivo_A).confere_existencia() == True:
        Fase_4(path_arquivo_A).abre_arquivo_adiciona()
        
    Fase_4(path_arquivo_B).abre_cria_edita_arquivo()

if __name__ == '__main__':
    main()