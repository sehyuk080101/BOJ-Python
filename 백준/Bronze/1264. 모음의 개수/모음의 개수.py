vowel = ["a", "e", "i", "o", "u"]
while True:
    n = 0
    w = input()
    if w == "#":
        break
    for i in w.lower():
        if i in vowel:
            n += 1
    print(n)