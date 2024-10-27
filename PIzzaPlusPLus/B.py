linha, coluna = [int(x) for x in input().split()]

array = [int(x) for x in input().split()]

id =  array.index(max(array))

l = id // coluna
c = id % coluna

print("A pizza de Mucarela esta localizada na linha {}, coluna {}".format(l, c))