fibo = 0
fibo1 = 1
fibo2 = 0
numero = 0

vezes = input('Qual o salto desejado para o resultado de Fibonacci? ')

for numero in range(int(vezes)):
    
    
    fibo = fibo1 + fibo2
    fibo1 = fibo2
    fibo2 = fibo
    print(fibo1)