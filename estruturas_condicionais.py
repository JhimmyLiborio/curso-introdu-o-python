# Aula 02 - Estrutura condicionais e operadores lógicos.


modelo_triangulo = "não encontrado"


lado_a = int( input( 'Qual o valor do lado A do triângulo ? ' ) )
lado_b = int( input( 'Qual o valor do lado B do triângulo ? ' ) )
lado_c = int( input( 'Qual o valor do lado B do triângulo ? ' ) )




if lado_a ==  lado_b and lado_a == lado_c:
    modelo_triangulo = "Equilatero"
elif lado_a != lado_b and lado_b != lado_c:
    modelo_triangulo = "Escaleno"
else:
    modelo_triangulo = "Isósceles"


print(modelo_triangulo)