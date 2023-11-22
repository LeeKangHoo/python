temp = input()

m = o = b = i = s = False
answer = False

for j in range(len(temp)):
    if temp[j] == 'M':
        m = True
    elif temp[j] == 'O':
        o = True
    elif temp[j] == 'B':
        b = True
    elif temp[j] == 'I':
        i = True
    elif temp[j] == 'S':
        s = True

if m:
    if o:
        if b:
            if i:
                if s:
                    answer = True


if answer:
    print("YES")
else:
    print("NO")
