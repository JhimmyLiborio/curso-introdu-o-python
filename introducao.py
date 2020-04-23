# variaéveis
# tipadas dinamicamente
# fortemente tipadas


a = 10;
b = 5;

soma =  a + b

#verificar o tipo de um variável em python
type (a)


#converter um tipo interiro para string
str(soma)


soma  = a + b
print( "Soma = " + str( soma ) )

subtracao = a-b;

print( "Subtração = " + str( subtracao ) )

multiplicacao = a * b
print( "Multiplicação  = " +  str( multiplicacao ) )


divisao = a / b
print( "Divisão = " + str( divisao ) )


resto =  a%b
print ( "Módulo = " + str( resto) )


#utilizando o .format para formatar valor em uma string

print ( "============================================" )
print ( ".format para formatar um valor em uma string" )


print( "Soma = {} ; Subtração = {} ; Multiplicação = {} " 
.format( soma, subtracao, multiplicacao ) )



#interação com o usuário com conversão de string para inteiro

idade = int ( input(" Digite sua idade: ") )
ano_nascimento = 2020 - idade;

print( " Sua idade é {} e você nasceu em {} " 
.format( idade, ano_nascimento ) )
