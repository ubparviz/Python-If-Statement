# Bank omonati foizlari

sum = float(input("Summani kiriting: "))

if sum < 100_000:
    print("5%")

if sum >= 100_000 and sum <= 500_000:
    print("7%")

if sum > 500_000:
    print("10%")