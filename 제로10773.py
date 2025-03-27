num = int(input())
stack = []
for i in range(0,num):
    a = int(input())
    if a == 0:
        if len(stack) != 0:
            stack.pop()
    else:
        stack.append(a)

print(sum(stack))

