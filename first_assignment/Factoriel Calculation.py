
n = int(input())
product = 1

if n == 0 or n == 1:
    product = 1
elif n == 2:
    product = 2
else:
    for i in range(1, n+1):
        product = product * i


print(product)
