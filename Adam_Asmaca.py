name=input("Adınızı Giriniz : ")
secret_word = input("Tahmin Edilecek Kelimeyi Giriniz : ")
secret_word_upper=secret_word.upper()
for item in list(range(40)):
    print(" ")
print("Hoşgeldin "+name+ " Hadi Adam Asmaca Oynayalım.")

guess_str=""

lives = 6

while lives > 0:

    character_left=0

    for character in secret_word_upper:

        if character in guess_str:
            print(character)
        else:
            print("-")
            character_left+=1

    if character_left==0:
        print(f"Cevap {secret_word_upper} Kazandiniz.")
        break

    guess=input("Tahminini Yaz : ")

    guess_upper=guess.upper()

    guess_str += guess_upper

    if guess_upper not in secret_word_upper:
        lives -= 1
        print("Yanliş Tahmin")
        print(f"{lives} Canın Kaldı")

        if lives == 0:
            print("Kaybettin")
            print("Oyun Bitti")
