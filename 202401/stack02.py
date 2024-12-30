import sys
input = sys.stdin.readline
N = int(input())
stack_li = list()


for _ in range(N):
    order = list(map(int, input().split()))
    if order[0] ==1 and order[1]:
        stack_li.append(order[1])
    if order[0] == 2:
        if stack_li:
            print(stack_li.pop())
        else:
            print(-1)
    if order[0] == 3:
        print(len(stack_li))
    if order[0] == 4:
        if stack_li:
            print(0)
        else:
            print(1)
    if order[0] == 5:
        if stack_li:
            print(stack_li[-1])
        else:
            print(-1)
