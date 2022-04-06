n = 0

n_2 = str(bin(n))
a = len(set(n_2[2::2]))
b = len(set(n_2[3::2]))
c = len(set(n_2[2:4]))

if (a == 0) or (b == 0):
    print("True", a,b)

if (a == 1) and (b == 1) and (c == 2):
    print("True", n_2)
else:
    print("False", n_2)
