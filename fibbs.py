# Recursion Task
def fibo(x):
    if x <= 1:
        return x
    else:
        return (fibo(x - 1) + fibo(x - 2))


num = int(input(" Give your Number"))
for x in range(0, num):
    print(fibo(x), end = " ")
