import sys

n = int(sys.stdin.readline())
queue = [0] * n
front = -1
rear = -1
size = 0

for i in range(n):
    a = sys.stdin.readline().split()
    if a[0] == "push":
        rear += 1
        queue[rear] = int(a[1])
        size += 1
    elif a[0] == "pop":
        if front != rear:
            front += 1
            print(queue[front])
            queue[front] = 0
            size -= 1
        else:
            print(-1)
    elif a[0] == "size":
        print(size)
    elif a[0] == "empty":
        print(int(front == rear))
    elif a[0] == "front":
        if front != rear:
            print(queue[front + 1])
        else:
            print(-1)
    elif a[0] == "back":
        if front != rear:
            print(queue[rear])
        else:
            print(-1)
