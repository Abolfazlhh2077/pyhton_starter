import math

n = int(input())
sum = 0

for i in range (1,math.floor((n/2)+1)):
    if n%i == 0:
       sum += i

if n == sum:
    print("YES")
else:
    print("NO")