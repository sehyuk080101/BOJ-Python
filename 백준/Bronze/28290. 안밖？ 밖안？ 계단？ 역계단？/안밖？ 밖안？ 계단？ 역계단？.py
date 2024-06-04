tb = {"fdsajkl;" : "in-out", "jkl;fdsa" : "in-out", "asdf;lkj" : "out-in", ";lkjasdf" : "out-in", "asdfjkl;" : "stairs", ";lkjfdsa" : "reverse"}

w = input()
if w in tb:
    print(tb[w])
else:
    print("molu")