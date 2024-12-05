import sys

heap = [0]
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n == 0:
        size = len(heap) - 1
        if size == 0:
            print(0)
        else:
            print(heap[1])
            last = heap[size]
            p = 1
            i = 2
            while i <= size:
                if i < size and heap[i] > heap[i + 1]:
                    i += 1
                if last <= heap[i]:
                    break
                heap[p] = heap[i]
                p = i
                i *= 2
            heap[p] = last
            heap.pop()
    else:
        heap.append(n)
        i = len(heap) - 1
        while i != 0 and n < heap[i // 2]:
            heap[i] = heap[i // 2]
            i //= 2
        heap[i] = n