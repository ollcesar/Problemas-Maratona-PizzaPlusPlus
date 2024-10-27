posicao = [int(x) for x in input().split()]

n = int(min(posicao))

n = posicao.index(n)+1

print("{} posicao".format(n))