number = int(input("Informe o número desejado: "))
isPrime = True

for i in range(2, number):
    if number % i == 0:
        isPrime = False

print(isPrime and "É primo" or "Não é primo")
