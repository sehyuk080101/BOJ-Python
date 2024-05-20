a = int(input())
num = a
for i in range(a):
	print(" "*(a-num), end="")
	for j in range(num):
		print("*", end="")
	print()
	num -= 1