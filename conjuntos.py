#====================================================================#
# Título: Organizando conjuntos e subconjuntos  de elementos
# O que é um conjunto?
# Conjunto não permite duplicidade
# Na sintaxe de Python um conjunto tem por caracteristica '{}' chaves
#=====================================================================#


# criar conjunto
print( '\n' )

print( 'Conjunto de elementos: ') 
conjunto = { 1, 2, 3, 4}
print( conjunto )


# adicionar elemento ao conjunto

print( 'Adicionar elementos ao conjunto: ')
conjunto.add( 5 )
print( conjunto )


# remover um elemento do conjunto

print( 'Remover elemento do conjunto: ')
conjunto.discard( 5 )
print( conjunto )


# união de conjuntos, a união ordena os elementos.
print ( '\n' )


conjunto_a = { 1, 3, 2, 4, 5 }
print( 'Conjunto A: {} '.format( conjunto_a) )
conjunto_b = { 5, 6, 7, 8, 9 }
print( 'Conjunto B: {} '.format( conjunto_b) )

conjunto_uniao = conjunto_a.union( conjunto_b )
print( 'Conjunto União: {} '.format( conjunto_uniao ) )

# intersecção de conjuntos

conjunto_interseccao = conjunto_a.intersection(conjunto_b)
print( 'Conjunto |A| Intersecção : {} '.format( conjunto_interseccao ) )


# diferença entre conjuntos

conjunto_diferença = conjunto_a.difference(conjunto_b)
print( 'Conjunto |A| Diferença: {}'.format( conjunto_diferença ) )


# diferença simétrica,  retorna o que há de diferente nos dois conjuntos
conjunto_diferenca_simetrica =  conjunto_a.symmetric_difference(conjunto_b)
print( 'Conjunto |A e B| Diferença Simétrica: {} '.format( conjunto_diferenca_simetrica) )





#=======================================================================
# Subconjuntos
# É um conjunto que possui outro conjunto
#=======================================================================


conjunto_a = { 1, 2, 3}
conjunto_b = { 1, 2, 3, 4, 5}

print( 'Conjunto A: {}'.format( conjunto_a ) )
print( 'Conjunto B: {}'.format( conjunto_b ) )

subconjunto = conjunto_a.issubset( conjunto_b )
print( 'Conjunto A é subconjunto de B ?  {} '.format( subconjunto) )
subconjunto = conjunto_b.issuperset( conjunto_b )
print( 'Conjunto B é superconjunto de A ? {} '.format( subconjunto) )



# Converter lista para conjunto
# Pode ser interesante para tirar duplicidade de lista

print ( 'Converter uma lista para conjunto: ')

lista_sorteio = [1, 2, 3, 4, 1, 2]
print( lista_sorteio)

conjunto =  set(lista_sorteio)
print( 'Lista convertidada para conjunto, sem duplicidade: {} '.format( conjunto ) )

# Converter a lista de voltar para conjunto
lista_sorteio = list( conjunto )
print( 'Conjunto convertido para lista, sem duplicidade: {} '.format( lista_sorteio ) )






