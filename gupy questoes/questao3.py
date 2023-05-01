import json
from datetime import datetime
from statistics import mean

# Carrega o arquivo JSON com os dados de faturamento
with open('faturamento.json') as f:
    faturamento = json.load(f)

# Converte as datas em formato string para objeto datetime
for dia in faturamento:
    dia['data'] = datetime.strptime(dia['data'], '%Y-%m-%d')

# Filtra os dias úteis (segunda a sexta-feira)
dias_uteis = [dia for dia in faturamento if dia['data'].weekday() < 5]

# Calcula o menor e o maior valor de faturamento
menor_valor = min(dia['valor'] for dia in dias_uteis)
maior_valor = max(dia['valor'] for dia in dias_uteis)

# Calcula a média mensal de faturamento (considerando apenas dias úteis)
media_mensal = mean(dia['valor'] for dia in dias_uteis)

# Conta quantos dias tiveram faturamento acima da média mensal
dias_acima_media = len([dia for dia in dias_uteis if dia['valor'] > media_mensal])

# Imprime os resultados
print(f'Menor valor de faturamento: R$ {menor_valor:.2f}')
print(f'Maior valor de faturamento: R$ {maior_valor:.2f}')
print(f'Número de dias com faturamento acima da média mensal: {dias_acima_media}')
