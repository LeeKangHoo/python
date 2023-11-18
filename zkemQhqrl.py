a = input()
b = a.split()

b = [int(i) for i in b]

N = b[0]
M = b[1]
K = b[2]

O1 = M
X1 = N-M

O2 = K
X2 = N-K

s = min(O2,O1) + min(X1,X2)
print(s)
