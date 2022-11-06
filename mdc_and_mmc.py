n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
indexMMC = 2
factorsMMC = []
indexMDC = 2
factorsMDC = []


def calculateMMC(number1, number2, index, factors, mmc):
    while (number1 != 1) or (number2 != 1):
        if number1 % index == 0 and number2 % index == 0:
            number1 = number1 / index
            number2 = number2 / index
            factors.append(index)
            index = 2
        else:
            if number1 % index == 0:
                number1 = number1 / index
                factors.append(index)
                index = 2
            elif number2 % index == 0:
                number2 = number2 / index
                factors.append(index)
                index = 2
            else:
                index += 1

    for i in range(len(factors)):
        mmc *= factors[i]

    return mmc


def calculateMDC(number1, number2, index, factors, mdc):
    while number1 != 1 or number2 != 1:
        if number1 % index == 0 and number2 % index == 0:
            number1 = number1 / index
            number2 = number2 / index
            factors.append(index)
            index = 2
        else:
            if number1 % index == 0:
                number1 = number1 / index
                index = 2
            elif number2 % index == 0:
                number2 = number2 / index
                index = 2
            else:
                index += 1

    for i in range(len(factors)):
        mdc *= factors[i]

    return mdc

print(f"MMC ({n1}, {n2}) = {calculateMMC(n1, n2, indexMMC, factorsMMC, 1)}")
print(f"MDC ({n1}, {n2}) = {calculateMDC(n1, n2, indexMDC, factorsMDC, 1)}")
