# Telefon raqami operatorini aniqlash

number = int(input("Raqam kiriting: "))

if number == 90 or number == 91:
    print("Ucell")

if number == 93 or number == 94:
    print("Beeline")

if number == 95 or number == 97:
    print("Uzmobile")

if number == 88 or number == 99:
    print("MobiUz")

if number != 90 or 91 or 93 or 94 or 95 or 97 or 88 or 99:
    print("Noma'lum operator")