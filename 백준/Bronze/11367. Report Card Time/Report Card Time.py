for i in range(int(input())):
    n, g = input().split()
    g = int(g)
    print(n, end = " ")
    if g >= 97:
        print("A+")
    elif g >= 90:
        print("A")
    elif g >= 87:
        print("B+")
    elif g >= 80:
        print("B")
    elif g >= 77:
        print("C+")
    elif g >= 70:
        print("C")
    elif g >= 67:
        print("D+")
    elif g >= 60:
        print("D")
    else:
        print("F")