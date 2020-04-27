#Como organizar dados em listas ou tuplas


lista_animal = ['Cachorro', 'Gato', 'Sapo', 'Cavalo', 'Papagaio']

# Imprimir uma lista

for animal in lista_animal:
    print ( animal )

# Organizando uma listar
print( '\n' )

lista_animal.sort()
print ( lista_animal )

# Remover um elemento conhecido da lista
print( '\n' )

lista_animal.remove( 'Cachorro' )
print ( lista_animal) 

# Remover o ultimo elemento da lista
# O método 'pop' retorna o elemento removido
# O método 'del' apenas remove
print( '\n' )

lista_animal.pop()
print ( lista_animal )

# Remover o primeiro elemento da lista
print( '\n' )

lista_animal.pop(0)
print ( lista_animal )

del lista_animal [0]
print ( lista_animal )

# Adicionar elementos na lista
print( '\n' )

lista_animal.append( 'Cachorro')
lista_animal.append( 'Cavalo' )
lista_animal.append( 'Sapo' )
lista_animal.append( 'Gato' )
lista_animal.sort()

print ( lista_animal )


# Realizar busca em uma lista
print ( '\n' )

buscar_nome = input( 'Qual animal procuras ? ' )

if buscar_nome in lista_animal:
    print ( 'Seu {} foi encontrado'.format(buscar_nome) )
else:
    print ( 'Lamento, não temo gato! ')


# Coceito de tupla: é imutável não aceita alterações de valores, 
# Mas pode ser ordenada
print ( '\n' )

tupla_animal = ('Cachorro', 'Gato', 'Cavalo', 'Sapo', 'Papagario')
print ( tupla_animal)


# Converter uma tupla em uma lista
print ( '\n' )

nova_lista_animal =  list(tupla_animal)
print ( nova_lista_animal )


# Converter uma lista em tupla
print ( '\n' )

nova_tupla_animal = tuple( lista_animal)
print ( nova_tupla_animal )
