sayı = int(input("Bir Sayı Giriniz :"))

count = 0
for i in range(1, sayı+1):
    if not (sayı % i) : 
        count += 1

if (sayı == 0) or (sayı == 1) or (count >= 3):
    print(sayı, "Asal sayı değil")
else :
    print(sayı, "Asal sayı")