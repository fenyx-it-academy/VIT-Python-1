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
Ad = input("Adiniz:")
Soyad = input("Soyadiniz:")
Yazi = " {} {} " .format(Ad, Soyad)
print("I", '*'*len(Yazi), "I", sep="")
print("I", ' '*len(Yazi), "I", sep="")
print("I", ' '*len(Yazi), "I", sep="")
print("I", Ad, Soyad, "I", sep=" ")
print("I", ' '*len(Yazi), "I", sep="")
print("I", ' '*len(Yazi), "I", sep="")
print("I", '*'*len(Yazi), "I", sep="")

#Soru 6 cevabi
while True:
    Start = input("Hallo! Heb je zin om met mij te praten? (Ja/Nee) ")
    if Start.lower() == "ja":
        print("Geweldig! Ik kijk ernaar uit om met iemand te praten.")
    elif Start.lower() == "nee":
        print("Wat jammer! Ik voel me erg verdrietig.")
        Tweede = input("Wil je me niet steunen? (Ja/Nee) ")
        if Tweede.lower() == "ja":
            print("Wat jammer! Dag.")
            exit()
        else:
            print("Heel bedankt.")
    else:
        print("Sorry, ik begrijp niet. Probeer het opnieuw.")
        continue

    while True:
        Derde = int(
            input("Je mag met mij praten als je volwassen bent. Hoe oud ben je? "))
        if Derde >= 18:
            print("Je bent al {}. Perfecte leeftijd!" .format(Derde))
        else:
            print("Je bent pas ", Derde, ".",
                  "Je mag niet met mij praten behalve onder begeleiding van je ouders.", sep="")
            print("Je kan later met mij praten onder toezicht van je ouders.")
            exit()
        Vierde = input("Hoe heet je of hoe kan ik je noemen? ")
        print("Merhaba ", Vierde, "!", sep="")
        Vijfde = input("Wat wil je graag doen in je vrije tijd? ")
        print("Leuk! Ik houd van wandelen in het park en lezen in mijn vrije tijd.")
        Zesde = input("Wat is het laatste boek dat je hebt gelezen?")
        print("Oh, ik heb dat boek ook gelezen! Wat vond je ervan?")
        while True:
            Zevende = input("Heb je het boek leuk gevonden? (Ja/Nee)")
            if Zevende.lower() == "ja":
                print("Ik ben blij dat je het leuk vond! Ik heb het ook leuk gevonden.")
            elif Zevende.lower() == "nee":
                print("Jammer dat je het niet leuk vond.")
            else:
                print("Ik begrijp niet.")
                continue
            print("Het was leuk om met je te praten, ",
                  Vierde, ".", " Tot ziens!", sep="")
            exit()
