# Uchburchak turi

print("Uchburchakni tomonlarini yozing")
a = float(input("tomon1: "))
b = float(input("tomon2: "))
c = float(input("tomon3: "))

if a == b and a ==c:
    print("Teng tomonli uchburchak")

elif a == b or a == c or b == c:
    print("Teng yonli uchburchak")

else:
    print("Turli tomonli uchburchak")