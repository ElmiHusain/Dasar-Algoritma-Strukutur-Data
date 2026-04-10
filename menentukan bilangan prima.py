n = int(input("masukkan angnka : "))
if n < 1:
    print("bukan bilangan prima")
else :
    is_prima = True
    for i in range (2, n):
        if n % i == 0:
            is_prima = False
            break
    
    if is_prima:
        print("bilangan prima")
    else:
        print("bukan bilangan prima")