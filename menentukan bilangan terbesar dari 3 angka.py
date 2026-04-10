a = int(input("masukkan nilai 1 = "))
b = int(input("masukkan nilai 2 = "))
c = int(input("masukkan nilai 3 = "))

if a >= b and a >= c:
    terbesar = a
elif b >= a and b >= c:
    terbesar = b
else:
    terbesar = c
print("Terbesar:", terbesar)