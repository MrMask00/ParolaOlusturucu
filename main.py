import random

# Kullanıcının parolasının içerebileceği karakterler
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# Kullanıcıdan parola uzunluğunu alma
parola_uzunlugu = int(input("Parola uzunluğunu girin: "))

# Oluşturulan paarolayı saklammma
olusturulan_parola = ""

# Belirtilen uzunlukta rastgele karakterleri seçerek parolayı oluşturun
for _ in range(parola_uzunlugu):
    rastgele_karakter = random.choice(karakterler)
    olusturulan_parola += rastgele_karakter

# Oluşturulan parola
print("Oluşturulan Parola: ", olusturulan_parola)
