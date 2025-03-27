import sys
num = int(input())
stack = []
for i in range(0,num):
    com = sys.stdin.readline().rstrip()
    c = com.split()
    if c[0] == 'push':
        stack.append(c[1])
    elif c[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif c[0] == 'size':
        print(len(stack))
    elif c[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

