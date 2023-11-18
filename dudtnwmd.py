a = input()
b = input()
s = 0
for i in range(int(b)):
    c = input()
    d = c.split()
    d = [int(i) for i in d]
    s += d[0] * d[1]
if int(a) == s:
    print("Yes")
else:
    print("No")


