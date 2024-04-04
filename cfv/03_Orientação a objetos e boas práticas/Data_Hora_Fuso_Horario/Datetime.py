from datetime import date, datetime, time, timedelta, timezone
#pip install pytz
import pytz

d = date(2024, 3, 28)
print(d)
print(date.today())

data_hora = datetime(2024, 3, 28, 11, 55, 00)
print(data_hora)
data_hora = datetime(2024, 3, 28)
print(data_hora)
print(datetime.today())
hora = time(11, 59)
print(hora)

tipo_carro = 'P'
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)

print(date.today() - timedelta(days=1))
print(f'O carro chegou as {data_atual} e ficará pronto às {data_estimada}')

data_hora_atual = datetime.now()
data_hora_str = "2024-03-28 12:21"
mascara_ptbr = "%d/%m/%y"
mascara_en = "%Y-%m-%d %H:%M"

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(data_convertida.strftime("%Y"))

data = datetime.now(pytz.timezone('Europe/Oslo'))
print(data)

data = datetime.now(timezone(timedelta(hours=2)))
print(data)
data = datetime.now(timezone(timedelta(hours=-3)))
print(data)
