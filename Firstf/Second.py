n = int(input("Введите число: "))
i = 2
first = []
while i <= n:
    if n % i == 0:
        first.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(first)