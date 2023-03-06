#Soru 1 cevabi
# Dairenin Alanini Hesaplama Programi
print("Dairenin alanini hesaplama programina hosgeldiniz.")
Yaricap = int(input("Dairenin Yaricapini Cm cinsinden Giriniz:"))
# round, Alan hesabinin cok kusuratli olmasini engelliyor.
Alan = round(3.1415 * Yaricap ** 2)
# Yazacagimiz yaziyi STR ye cevirmenin bir yolu.
Yazi = "Dairenin Alani: {} cm2'dir." .format(Alan)
print(type(Yazi))
print(Yazi)
print('-'*len(Yazi))

#Soru 2 cevabi
Ad = input("Adiniz: ")
Soyad = input("Soyadiniz: ")
print("Merhaba", Soyad, Ad, "!",sep="   ")

#Soru 3 cevabi
Ad = input("Adiniz: ")
Soyad = input("Soyadiniz: ")
Adres = input("Adresiniz: ")
print(Ad, Soyad, Adres, "*"*len(Adres), sep="\n")

#Soru 4 cevabi
SaniyeDegeri = int(input("Lutfen saniye degerini giriniz:"))
DakikaSaniye = 60  # 1 dk 60 saniyedir.
SaatSaniye = 60*DakikaSaniye  # 1 saat 60*60 saniye,
GunSaniye = 24*SaatSaniye  # 1 Gun 24*60*60 saniyedir.
# Eger girilen deger icerisinde 1 gun varsa, bunu bulmak icin girilen degeri 1 gun icindeki saniyeye bolmeliyiz.
Gun = SaniyeDegeri//GunSaniye
GundenArtan = SaniyeDegeri % GunSaniye
Saat = GundenArtan//SaatSaniye
SaattenArtan = GundenArtan % SaatSaniye
Dakika = SaattenArtan//DakikaSaniye
Saniye = SaattenArtan % DakikaSaniye
print("{} Saniye\n {} Gun,\n {} Saat,\n {} Dakika,\n {} Saniyedir." .format(
    SaniyeDegeri, Gun, Saat, Dakika, Saniye))

#Soru 5 cevabi
