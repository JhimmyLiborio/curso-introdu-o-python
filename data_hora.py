##########################################
# Título: Manipulação de data e hora     #
##########################################


from datetime import date, time, datetime, timedelta


# Recuperar data  atual


data_atual = date.today()
print(data_atual)

# Alterar formatação de data

print( data_atual.strftime('%d/%m/%Y') )
print( data_atual.strftime('%d/%m/%y') )
print( data_atual.strftime('%A/%B/%Y') )



# Como gerar  um horário

hora_atual = time(hour=15, minute=10, second=30)
print( hora_atual)


# Retornar data e hora atual (Datetime)

data_hora_atual = datetime.now()
print( data_hora_atual )
print( data_hora_atual.strftime('%H:%M:%S'))
print( data_hora_atual.strftime('%c'))
print(data_hora_atual.year)
print(data_hora_atual.month)
print(data_hora_atual.weekday)
print(data_hora_atual.day)
print(data_hora_atual.hour)


# formatar um string para Datetime

data = '30/04/1989'
data_convertida = datetime.strptime(data, '%d/%m/%Y')
print(data_convertida)



# Realizar soma e subtração  de datas  com TimeDelta

nova_data =  data_convertida - timedelta(days=365, hours=0, minutes=0)
print(nova_data)

