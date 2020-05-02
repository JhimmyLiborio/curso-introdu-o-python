###############################################
# Título: Iterações                           #
# Estrtura de repetição: while e for          #
#                                             #
###############################################


# inicia em 0
for x in range (50):
    print(x)

# número primos

numero  = int( input(' Digite um  número: '))


for atual in range( 1, numero + 1 ):
    qtd_div = 0
    for x in range ( 1, atual + 1 ):
        if atual  % x == 0:
            qtd_div += 1

    if qtd_div ==  2:
        print( '{} é número primo '.format(atual) )
    else:
        print( '{} não é um número primo'.format(atual) )


