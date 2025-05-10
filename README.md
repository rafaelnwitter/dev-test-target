# dev-test-target

## Pré-requisitos

- Python 3.12 ou superior
- (Opcional) Ambiente virtual Python ativado


## Executando cada script individualmente

### 1. loop_simples.py
Soma os números de 1 até 13 usando um loop simples.

```bash
python loop_simples.py
```

### 2. fibonacci.py
Verifica se um número pertence à sequência de Fibonacci.

```bash
python fibonacci.py
```

### 3. rewards.py
Lê um arquivo de dados (`dados.json` ou `dados.xml`) e mostra menor, maior e dias acima da média de faturamento.

Por padrão, usa `dados.json` ou `dados.xml` presentes na raiz do projeto.

```bash
python rewards.py
```

### 4. string_reverse.py
Inverte os caracteres de uma string sem usar funções prontas.

```bash
python string_reverse.py
```

### 5. calc_percentual.py
Calcula o percentual de representação de cada estado em relação ao total mensal de faturamento.

```bash
python calc_percentual.py
```

## Executando todos os scripts em sequência

O arquivo `main.py` executa todos os scripts acima, um após o outro, com pequenas pausas entre eles.

```bash
python main.py
```

Durante a execução, alguns scripts podem solicitar entradas pelo terminal.

---

**Observação:**
- Certifique-se de que os arquivos `dados.json` e/ou `dados.xml` estejam presentes na raiz do projeto para o funcionamento do `rewards.py`.
- Para rodar em ambiente virtual, ative-o antes dos comandos acima.