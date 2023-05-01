num = int(input("Digite um número inteiro positivo: "))

fib = [0, 1]
while fib[-1] < num:
    next_fib = fib[-1] + fib[-2]
    fib.append(next_fib)

if num in fib:
    print(num, "pertence à sequência de Fibonacci.")
else:
    print(num, "não pertence à sequência de Fibonacci.")
