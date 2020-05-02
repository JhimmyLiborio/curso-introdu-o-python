###########################################
# Título: Lambda                         #
##########################################


# Lamda é uma função anônima, ouse ja não possui um nome, é um forma de simplificar algo que será utilizado várias
# Coisas simples são eficientes com lambda e  podem ser feitas em uma linha


# Ex: Contatdor de letras de uma lista

contador_letras = lambda lista: [ len(x) for x in lista ]


lista_animal = [ 'Cachorro', 'Cavalo', 'Peixe', 'Sapo' ]
print( contador_letras( lista_animal ) )


# Ex: Calculadora que soma dois números

soma =  lambda valor_a, valor_b: valor_a + valor_b

print ( soma( 10, 5))



# Dicionário Lambda

calculadora = {
    'soma': lambda a , b: a + b,
    'subtracao': lambda a , b: a - b,
    'divisao': lambda a , b: a / b,
    'multiplicacao': lambda a , b: a * b
}

soma =  calculadora['soma']

print ( soma( 10, 10 ))
