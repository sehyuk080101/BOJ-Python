alphabet = [-1] * 26
S = input()
for i in range(len(S)):
    if alphabet[ord(S[i]) - 97] == -1:
        alphabet[ord(S[i]) - 97] = i
print(*alphabet)