import json
import os
import xml.etree.ElementTree as ET

valores = []

if os.path.exists('dados.json'):
    with open('dados.json', 'r') as f:
        dados = json.load(f)
    valores = [dia['valor'] for dia in dados if dia['valor'] > 0]
elif os.path.exists('dados.xml'):
    tree = ET.parse('dados.xml')
    root = tree.getroot()
    for row in root.findall('row'):
        valor = float(row.find('valor').text)
        if valor > 0:
            valores.append(valor)
else:
    print('Nenhum arquivo de dados encontrado.')
    exit(1)

if not valores:
    print('Nenhum valor de faturamento encontrado.')
    exit(1)

menor = min(valores)
maior = max(valores)
media = sum(valores) / len(valores)
dias_acima_media = sum(1 for v in valores if v > media)

print(f"Menor valor de faturamento: {menor:.2f}")
print(f"Maior valor de faturamento: {maior:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
