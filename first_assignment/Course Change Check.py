

n = int(input())
Trigger = [5,5]
CourseChange = -1

for i in range(n):
    Trigger[0] = int(input())
    if Trigger[0] != Trigger[1]:
        CourseChange += 1
    Trigger[1] = Trigger[0]

print(CourseChange)
