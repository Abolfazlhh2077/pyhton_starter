
number = ""
for i in range(1, 5001):
    number += str(i)

k = int(input())

for i in range(5001):
    if i == k - 1:
        print(number[i])
        break