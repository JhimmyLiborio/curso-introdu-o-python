##############################
# Título: módulo             #
#                            #
##############################

# Módulo é cadas arquivo .py
# após a importação (import ) pode-se acessar  método ou atributo desse módulo
import orientacao_objetos

calculadora = orientacao_objetos.Calculadora( 20,40 )
print ( calculadora.soma() )

# se tive outras classes dentro de um arquivo.py
# pode-se especificar a classe  de um arquivo.py

from orientacao_objetos import Calculadora

calculadora = Calculadora( 60, 40 )
print( calculadora.multiplicacao() )