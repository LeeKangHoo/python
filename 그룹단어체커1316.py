num = int(input())
cnt = 0
for i in range(0,num):
    state = True
    n = []
    tmp = input()
    for j in tmp:
        if n == 0:
            n.append(j)
        elif j in n:
            if n[-1] != j:
                state = False
                break
        else:
            n.append(j)
    if state:
        cnt += 1
print(cnt)
