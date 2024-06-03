A, B, C = map(int, input().split())
D = int(input())
print(((A * 3600 + B * 60 + C + D) // 3600) % 24, (A * 3600 + B * 60 + C + D) % 3600 // 60, (A * 3600 + B * 60 + C + D) % 3600 % 60)