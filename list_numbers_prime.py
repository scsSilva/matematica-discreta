from datetime import timedelta, datetime

end_time = datetime.now() + timedelta(seconds=60)
number = 1
counter = 0

while True:
    if datetime.now() > end_time:
        print(f"Primos encontrados: {counter}")
        break
    else:
        if number == 2 or (2 ** (number - 1)) % number == 1:
           counter += 1
           print(number)
        number += 1
