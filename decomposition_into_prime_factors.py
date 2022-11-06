number = int(input("Informe o número desejado: "))
memory_number = number
factors = []
index = 2

while number != 1:
    if number % index == 0:
        number = number / index
        factors.append(index)
        index = 2
    else:
        index += 1

for i in range(len(factors)):
    if i == len(factors) - 1:
        print(f"{factors[i]}", end=" = ")

    else:
        print(f"{factors[i]} * ", end="")

print(f"{memory_number}", end="")
