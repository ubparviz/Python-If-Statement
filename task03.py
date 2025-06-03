# Harf katta yoki kichik

letter = input("letter kiriting: ")

if len(letter) == 1 and letter.isalpha():

    if letter.isupper():
        print("Katta harf")
    else:
        print("Kichik harf")

elif letter.isdigit():
    print("Raqam mumkin emas")

else:
    print("Faqat bitta harf kiriting!")