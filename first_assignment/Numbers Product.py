n = int(input())
digits = 0

while n != 0:
    digits += n % 10
    n = n // 10

    if n == 0 and digits > 9:
        n = digits
        digits = 0

print(digits)