# Ballar bo‘yicha baho

ball = int(input("Balingizni kiriting (1 dan 100 gacha): "))

if ball >= 90 and ball <= 100:
    print("A")

elif ball >= 80 and ball <= 89:
    print("B")

elif ball >= 70 and ball <= 79:
    print("C")

elif ball >= 60 and ball <= 69:
    print("D")

elif ball >= 0 and ball <= 59:
    print("F")

elif ball > 100 or ball < 0:
    print("Ball 0-100 oralig'ida bo'lishi kerak!")