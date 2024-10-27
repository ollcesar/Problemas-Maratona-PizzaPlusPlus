n = int(input())

s = []
s1 = set()

for i in range(n):
    m = [int(x) for x in input().split()]

    s += m
    s1 |= set(m)

l = 1

for el in s1:
    if s.count(el) > n:
        l = 0
        break

print(l)