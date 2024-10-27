frase = [(x) for x in input().split()]

frase2 = ""

for i in frase:
    for j in range(len(i)):
        if j % 2==0:
            continue
        frase2 += i[j]

    frase2 += " "

print(frase2)