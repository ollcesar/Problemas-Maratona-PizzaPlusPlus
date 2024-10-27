def fibona(n):
    if n <=1:
        return 1
    else:
        return fibona(n-1) + fibona(n-2)

n = int(input())

for i in range(n):
    num = int(input())

    print(fibona(num))