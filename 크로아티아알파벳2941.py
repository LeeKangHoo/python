alpha = input()
state = 0
cnt = 0
answer = 0

while True:
    if cnt >= len(alpha):
        break

    if alpha[cnt] == 'c':
        if cnt+1 < len(alpha) and (alpha[cnt+1] == '=' or alpha[cnt+1] == '-'):
            cnt += 2
            answer += 1
            continue
    if alpha[cnt] == 'd':
        if cnt+2 < len(alpha) and (alpha[cnt+1] == 'z' and  alpha[cnt+2] == '='):
            cnt += 3
            answer += 1
            continue
        elif cnt+1 < len(alpha) and alpha[cnt+1] == '-':
            cnt += 2
            answer += 1
            continue
    if cnt+1 <len(alpha) and (alpha[cnt] == 'l' and alpha[cnt+1] == 'j'):
        cnt += 2
        answer += 1
        continue
    if cnt+1 < len(alpha) and (alpha[cnt] == 'n' and alpha[cnt+1] == 'j'):
        cnt +=2
        answer += 1
        continue
    if cnt+1 < len(alpha) and (alpha[cnt] == 's' and  alpha[cnt+1] == '='):
        cnt += 2
        answer += 1
        continue
    if cnt+1 < len(alpha) and (alpha[cnt] == 'z' and alpha[cnt+1] == '='):
        cnt += 2
        answer += 1
        continue
    cnt += 1
    answer += 1

print(answer)

