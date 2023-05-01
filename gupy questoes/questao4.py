faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = sum(faturamento.values())

for estado, valor in faturamento.items():
    percentual = (valor / total) * 100
    print(f'{estado}: {percentual:.2f}%')
    
"""
    resultado = SP: 42.20%
    RJ: 22.84%
    MG: 18.22%
    ES: 16.90%
    Outros: 12.35%
"""