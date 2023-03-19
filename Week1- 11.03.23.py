#Soru1
pi = 3.14
r = (input("Dairenin yari capini girin:"))
r2 = int(r) ** 2
alan = r2 * pi
cevap = ("Dairenin alani:{} m2'dir".format(alan))
print(cevap, "\n", "-" * len(cevap),sep = "")


#Soru2
ad = input("Adiniz:")
soyad = input("Soyadiniz:")
print("Merhaba", soyad, ad, sep="   ")

#Soru3
ad = input("Adiniz:")
soyad = input("Soyadiniz:")
adres = input("Adresiniz:")
print(ad, soyad, adres, sep="\n")
print("*" * len(adres))

#Soru4
sani = input("Sureyi saniye olcu biriminde girin:")
saniye = int(sani)
dakika = saniye // 60
saat = dakika // 60
gun = saat // 24
print("{} gun,{}saat,{}dakika,{}saniye".format(gun,saat,dakika,saniye))

#Soru5
ad = input("Adiniz:")
soyad = input("Soyadiniz:")
print("-" * 30)
print("|",ad + " " + soyad,"|",sep="\t")
print("-" * 30)

#Soru6
print("Merhaba. Ben yeni bir chat programinin demo versiyonuyum. Adim Chat0.")
ad = input("Adin ne?:")
print("Tanistigimiza memnun oldum", ad)
durum = input("Nasilsin?")
print("Umarim daha iyi olursun.", ad)
dil = input("Anadilin disinda kac dil biliyorsun?")
print(dil, "Bu cok iyi. Kendini gelistirmeye devam etmelisin. Her lisan bir insan.")
mesgul = input("Su siralar ne ile mesgulsun?")
print(mesgul,"Senin ici oldukca onemli olmali.")
kitap = input("Gunluk kac sayfa kitap okursun?")
print(kitap,"Onemli olan sayfa sayisi degil. Surekli ve efektif okumak.")
yemek = input("En sevdigin yemek nedir?")
print("Kulaga oldukca lezzetli geliyor.")
