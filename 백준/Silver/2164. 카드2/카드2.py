n = int(input())
front = -1
rear = n - 1
queue = [i for i in range(1, n + 1)]
while rear - 1 != front:
    front += 2
    queue.append(queue[front])
    rear += 1

print(queue[rear])