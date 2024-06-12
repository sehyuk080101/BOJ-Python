A, B, C = map(int, input().split())
D = int(input())
t = A * 3600 + B * 60 + C + D
print(t // 3600 % 24, t % 3600 // 60, t % 3600 % 60)