#############################################
# Título: Métodos, Funções e Classes       #
#                                          #
############################################

# Declaração de classe
class Calculadora:
    
#inicializar valores dentro de uma classe

    def __init__(self):
        pass

    def __init__(self, x, y):
        self.valor_a = x
        self.valor_b = y
      

# Declaração de métodos 



    def soma ( self):
        return self.valor_a + self.valor_b


    def sosubtracao ( self ): 
        return self.valor_a - self.valor_b

    def multiplicacao ( self ):
        return self.valor_a * self.valor_b

    def divisao ( self ):
        if (self.valor_b != 0):
            return self.valor_a / self.valor_b
        else:
            return 0


if __name__ == 'main':
    calculadora = Calculadora( 10, 0 )
    print( calculadora.divisao() )
