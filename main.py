import time
import subprocess
import sys
import os
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

EXERCICIOS = [
    {
        'nome': 'loop_simples.py',
        'escopo': 'Soma os números de 1 até 13 usando um loop simples.',
        'input': 'Nenhuma entrada é necessária.'
    },
    {
        'nome': 'fibonacci.py',
        'escopo': 'Verifica se um número pertence à sequência de Fibonacci.',
        'input': 'Informe um número inteiro.'
    },
    {
        'nome': 'rewards.py',
        'escopo': 'Lê um arquivo de dados (dados.json ou dados.xml) e mostra menor, maior e dias acima da média de faturamento.',
        'input': 'Informe o caminho do arquivo de dados (json ou xml), ou pressione Enter para usar o padrão.'
    },
    {
        'nome': 'string_reverse.py',
        'escopo': 'Inverte os caracteres de uma string sem usar funções prontas.',
        'input': 'Digite uma string.'
    },
    {
        'nome': 'calc_percentual.py',
        'escopo': 'Calcula o percentual de representação de cada estado em relação ao total mensal de faturamento.',
        'input': 'Nenhuma entrada é necessária.'
    }
]

def run_exercicio(ex):
    print("\n" + "="*40 + "\n")
    logger.debug(f"Executando {ex['nome']}...\n")
    print(f"--- {ex['nome']} ---")
    print(f"Escopo: {ex['escopo']}")
    print(f"O que informar: {ex['input']}")
    # Para rewards.py, perguntar sobre arquivo
    if ex['nome'] == 'rewards.py':
        resp = input("Deseja informar o caminho do arquivo de dados? (s/n): ").strip().lower()
        if resp == 's':
            caminho = input("Informe o caminho do arquivo (json ou xml): ").strip()
            if os.path.exists(caminho):
                ext = os.path.splitext(caminho)[1].lower()
                if ext == '.json':
                    os.replace(caminho, 'dados.json')
                elif ext == '.xml':
                    os.replace(caminho, 'dados.xml')
                else:
                    logger.warning("Arquivo não reconhecido. Usando padrão.")
            else:
                logger.warning("Arquivo não encontrado. Usando padrão.")
    print()  # Linha em branco antes de rodar o script
    subprocess.run([sys.executable, ex['nome']])
    print("\n" + "-"*40 + "\n")

def main():
    print("\n================ INÍCIO DOS EXERCÍCIOS ================\n")
    for idx, ex in enumerate(EXERCICIOS):
        logger.debug(f"Próximo: {ex['nome']}")
        run_exercicio(ex)
        if idx < len(EXERCICIOS) - 1:
            print("Aguardando 5 segundos para o próximo exercício...\n")
            time.sleep(5)
    print("\n================= FIM DOS EXERCÍCIOS =================\n")
    logger.debug("Todos os exercícios executados.")

if __name__ == "__main__":
    main()
