########################################
# Título: Manipulação de arquivos      #
########################################

# módulo para copiar e mover arquivos na árvore de diretório
import shutil




# 'open' abrir um arquivo, ou criar um arquivo se não existe
# 'w' escrever, sobrepõe se já contiver escrita
# 'a' atualizar  arquivo
# 'r' ler arquivo
arquivo = {

    'escrever': lambda texto: open('arquivo.txt', 'w').write(texto),
    'atualizar': lambda texto: open('arquivo.txt', 'a').write(texto),
    'ler': lambda : open('arquivo.txt', 'r').read()
}


apontador = arquivo['escrever']
apontador('Minha primeira escrita\n')

apontador = arquivo['atualizar']
apontador('Minha primeira atualização de arquivo')

apontador = arquivo['ler']
leitura = apontador().split('\n')

for linha in leitura:
    print(linha)


def copiar_arquivo( nome_arquivo ):
    shutil.copy(nome_arquivo, '/home/jhimmy/')

def mover_arquivo ( nome_arquivo ):
    pass
    #shutil.copy(nome_arquivo, '/home/jhimmy/')
    


if __name__ == "__main__":
    copiar_arquivo('arquivo.txt')