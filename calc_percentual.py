# Programa para calcular o percentual de representação do faturamento por estado

def calcular_percentuais(faturamento_estados):
    total = sum(faturamento_estados.values())
    percentuais = {}
    for estado, valor in faturamento_estados.items():
        percentuais[estado] = (valor / total) * 100
    return percentuais

def solicitar_faturamento():
    print("\nInforme os dados no formato: UF:valor,UF:valor,...")
    print("Exemplo: SP:67836.43,RJ:36678.66,MG:29229.88,ES:27165.48,Outros:19849.53\n")
    entrada = input("Digite os dados: ").strip()
    faturamento_estados = {}
    try:
        for item in entrada.split(','):
            if not item:
                continue
            estado, valor = item.split(':')
            faturamento_estados[estado.strip()] = float(valor.strip())
    except Exception as e:
        print("\nFormato inválido. Usando valores padrão.\n")
        return None
    return faturamento_estados

def main():
    faturamento_padrao = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }
    print("Deseja informar um novo faturamento por estado?")
    resp = input("Digite 's' para sim ou pressione Enter para usar o padrão: ").strip().lower()
    if resp == 's':
        faturamento_estados = solicitar_faturamento()
        if not faturamento_estados:
            faturamento_estados = faturamento_padrao
    else:
        faturamento_estados = faturamento_padrao
    percentuais = calcular_percentuais(faturamento_estados)
    print("\nPercentual de representação por estado:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

if __name__ == "__main__":
    main()
