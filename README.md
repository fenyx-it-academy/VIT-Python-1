#Week1HomeworkAnswer1

print("\n","Dairenin Alanını Hesaplama", "\n")

cap=input("Dairenin Çapı: ")
yaricap=int(cap)/2
pi=3.14159
alan=pi*(yaricap*yaricap)

sonuc="Dairenin Alanı "+str(alan)+" cm2 dir"

print("\n", sonuc, "\n", "-"*len(sonuc), sep="")

input()

######################

#Week1HomeworkAnswer2

ad=input("Adınız: ")
soyad=input("Soyadınız: ")

print("Hoşgeldiniz", soyad, ad, sep=" "*3)

input()

######################

#Week1HomeworkAnswer3

ad=input("Adınız: ")
soyad=input("Soyadınız: ")
adres=input("Adresiniz: ")

print("\n", ad, "\n", soyad, "\n", adres, "\n", "*"*len(adres), sep="")

input()

#####################

#Week1HomeworkAnswer4

Baslik=str("SANİYE DÖNÜŞTÜRÜCÜYE HOŞGELDİNİZ")
print("\n", Baslik, "\n", "-"*len(Baslik), "\n")

Girdi=int(input("Saniye Giriniz:"))
Gün=Girdi//86400  ## Gün sayısını buluruz.
Saat=(Girdi%86400)//3600 ## Saat sayısını buluruz.
Dakika=(Girdi%3600)//60 ## Dakika sayısını buluruz.
Saniye=Girdi%60 ## Saniye sayısını buluruz.

print("\n", Girdi, "saniye;", Gün, "Gün", Saat, "Saat", Dakika, "Dakika", Saniye, "Saniyedir.","\n" )

######################

#Week1HomeworkAnswer5

#İçine yazılan AdSoyad boyutuna göre değişen dikdörtgen 

AdSoyad=input("Adınızı ve Soyadınızı Giriniz:")
LenAd=len(AdSoyad)

print("+"*(LenAd+6))
print("+"+" "*(LenAd+6-2)+"+")
print("+"+" "*1, AdSoyad, " "*1+"+")
print("+"+" "*(LenAd+6-2)+"+")
print("+"*(LenAd+6))

###################

#Week1HomeworkAnswer6

#Diyalog programı

print("\n","HOŞ GELDİNİZ!", "\n")
print("Açıklamalar:", "\n", "1- Adınızı veya Nickname'inizi istediğiniz bir şey seçebilirsiniz.", "\n", "2- Cevaplar evet ise 'E', hayır is 'H' olmalı.", "\n")
Adı=input("Adını öğrenebilir miyim?")
print("\n", "Merhaba", Adı, "iyi misin?", "\n")

Cevap1=input()

if Cevap1=="E":
    print("İyi olmana sevindim", Adı)
    
    
elif Cevap1=="H":
    print("\n", "Deprem herkesin psikolojisini etkiledi sanırım.", "\n")
    Cevap2=input("Bir terapist/psikolog ile görüşmek ister misin?")
    if Cevap2=="E": 
        print("\n", "Önerebileceğim alanında başarılı bir arkadaşım var.", "\n", "İletişim bilgileri: \n İnstagram: @PsikologAhmet \n Telefon: +31 1234567890")
    elif Cevap2=="H":
        print("\n", "Bir uzmanla konuşmak iyi gelebilirdi ancak tavsiyemi uygulamak zorunda değilsin elbette :)")


