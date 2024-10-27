ls = {}

n = int(input())

for i in range(n):
    nome = input()
    qnt = int(input())
    valorU = float(input())

    ls[nome] = [qnt, valorU, qnt, 0, 0]

op = 0

ls2 = []

op = int(input())

while op != -1:
    nome = input()

    ls[nome][2] -= op
    ls[nome][3] += op
    ls[nome][4] = ls[nome][2] * ls[nome][1]

    
    op = int(input())

nomes = list(ls.keys())
valores = list(ls.values())

for i in range(len(valores)):
    valores[i].insert(0, nomes[i])

valores = sorted(valores, key=lambda v: v[0])
valores = sorted(valores, key=lambda v: v[2])
valores = sorted(valores, key=lambda v: v[5], reverse=True)
valores = sorted(valores, key=lambda v: v[4], reverse=True)

print(valores)