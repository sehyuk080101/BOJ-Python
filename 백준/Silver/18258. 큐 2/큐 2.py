import sys

front = -1
rear = -1
queue = []

for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().split()
    if s[0] == "push":
        queue.append(s[1])
        rear += 1
    elif s[0] == "pop":
        if front == rear:
            print(-1)
        else:
            front += 1
            print(queue[front])
    elif s[0] == "size":
        print(rear - front)
    elif s[0] == "empty":
        if front == rear:
            print(1)
        else:
            print(0)
    elif s[0] == "front":
        if front == rear:
            print(-1)
        else:
            print(queue[front + 1])
    elif s[0] == "back":
        if front == rear:
            print(-1)
        else:
            print(queue[rear])