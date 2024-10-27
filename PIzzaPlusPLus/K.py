pi = 3.14159265

NP, QA = [int(x) for x in input().split()]
b, B, H = [int(x) for x in input().split()]

k = QA/NP

V = H*(B**2*pi - (b**4*pi)/(B**2))/3

if k > V:
    k = V

h = H*k*4/V

print(h)