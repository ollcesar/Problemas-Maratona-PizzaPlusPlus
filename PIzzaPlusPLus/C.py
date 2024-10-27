n = int(input())

for _ in range(n):
    num = int(input())

    num1 = num*1.5
    num2 = num1*0.75
    num3 = num2*1.5
    num4 = num3*0.75

    print(f"{num:.2f} {num1:.2f} {num2:.2f} {num3:.2f} {num4:.2f}")