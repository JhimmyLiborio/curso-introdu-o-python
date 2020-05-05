#################################################
#Título: Gerenciamento  de Exceções

#################################################

lista = [1,2]
try:
    divisao = 10 / 1
    lista = lista[1]
    #x = a
    print('try: pode ocorrer exeção: ')

except ZeroDivisionError:
    print( 'Não é possível realizar uma divisão por zero.' )
except IndexError:
    print( 'Posição não existente na lista!')
#pai de todas as exceções
except BaseException as e:
    print( 'Erro desconhecido. Erro: {}'.format(e))

else:
    print( 'else: Executa quando não ocorre exceção!')

finally:
    print( 'finaly: Sempre executa: essencial para algo que se deve fechar')


# Para fazer uma classe personalizada de Exeções cria uma classe que herda de Exception
class Error( Exception):
    pass

# Depois, crie uma classe que herde da classe que herda de Exceptio.format()
# Por convenção toda classe  Personalizada de Exeção deve terminar em 'Error'
class InputError (Error):

    def __init__(self, mensagem_erro):
          self.mensagem = mensagem_erro
    


contador_notas = 1
while True:
    
    try:
        
        nota = float( input( 'Registre  a nota {} : '.format( contador_notas ) ) )
        
        if nota > 10:
            raise InputError( 'Nota inválida! Digite uma nova menor ou igual a 10. ')
        if nota < 0:
            raise InputError( 'Nota inválida! Digite uma nova maior que ou igual a 0. ')
        if contador_notas ==  4:
            contador_notas = 0
            break

    except ValueError:
           print( 'Nota inválida! Caractere inválido. Exemplo de nota: 7.9 ' )
    except InputError as e:
           print( e )
    else:
        contador_notas += 1


