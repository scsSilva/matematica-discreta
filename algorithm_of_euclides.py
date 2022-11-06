n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))

def calculate(number1, number2):
    if (number1 % number2 == 0):
        return number2;
    else:
        return  calculate(number2, number1 % number2)

print(f"MDC({n1}, {n2}) = {calculate(n1, n2)}")
