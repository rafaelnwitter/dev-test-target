# Programa para verificar se um número pertence à sequência de Fibonacci

def pertence_fibonacci(numero):
    """
    Verifica se um número pertence à sequência de Fibonacci
    """
    if numero < 0:
        return False
    fib = [0, 1]
    while fib[-1] < numero:
        fib.append(fib[-1] + fib[-2])
    return numero in fib

def main():
    try:
        n = int(input("Informe um número: "))
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
        return
    if pertence_fibonacci(n):
        print(f"O número {n} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {n} NÃO pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
