fibonacci = [1, 1]
while fibonacci[-1] < 55:
    fibo_next = fibonacci[-2] + fibonacci[-1]
    fibonacci.append(fibo_next)
print(fibonacci)