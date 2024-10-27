entrada = [int(x) for x in input().split()]

if entrada[0] > entrada[1]:
    print("Pedro")
elif entrada[1] > entrada[0]:
    print("Patrícia")
else: 
    print("A Mesa do Prejuízo foi a vencedora!!!")