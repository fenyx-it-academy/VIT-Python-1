#soru 1
#Dairenin alanini hesaplamak icin ilk once kullanicidan input fonk 
#kullanarak bir yaricap alalim. 
#Ayrica daha sonra matematik islemi ypacagimiz 
#icin bu degeri int a cevirmeliyiz.
yaricap= int(input("Dairenin yaricapini cm cinsinden giriniz."))
#alan formulunu bir degere atiyoruz.
daireninAlani= 3.1415*(yaricap*yaricap)
#bilgisayardan aldigimiz degeri alti cizili olarak yazdirmak icin 
#bir cikti degeri olusturuyoruz. 
cikti= "Dairenin alani"+" "+str(daireninAlani)+" "+"cm2dir."
#bu degerin eleman sayisi kadar altini cizmek icin de len fonk kullaniyoruz.
print(cikti,"\n", "-"*len(cikti), sep="")

#soru 2
ad= input("Adiniz:")
soyad= input("Soyadiniz:")

print("Merhaba",soyad,"   ",ad,"!")
#soru 3
ad=input("Adiniz:")
soyad=input("Soyadiniz:")
adres=input("Adresiniz:")

print(ad,"\n",soyad,"\n",adres,"\n","*"*len(adres),sep="")

#soru 4
saniye=int(input("Saniye giriniz:"))
dakika=saniye//60
saniye=saniye%60
saat=dakika//60
dakika=dakika%60
gun=saat//24
saat=saat%24


print(gun,saat,dakika,saniye)

#soru 5
isimSoyisim=input("Isminizi ve soyisminizi giriniz:")

ustAlt="*"*(len(isimSoyisim)+10)
print(ustAlt)
yatay= "|"+" "*(len(isimSoyisim)+8)+"|"
print(yatay)
print(yatay)
fark=((len(ustAlt)-len(isimSoyisim))/2)-3
print("|"," "*int(fark),isimSoyisim," "*int(fark),"|")
print(yatay)
print(yatay)
print(ustAlt)

#soru 6
isim=input("Merhaba isminiz ve soyisminiz nedir?")
print("Merhaba",isim,"!","\n","Uygulamamiza hosgeldin!",sep="")
yas=input("Lutfen yasini gir:")
print(yas,"yasinda olmak cok guzeldir.")
yemek=input("En sevdigin yemek ne?")
print("Bu ne tesaduf!!! Benim de en sevdigim yemek",yemek,".")
okul=input("Nereden mezunsun?")
print("Bir arkadasim daha var senin gibi",okul,"dan mezun.")
ikamet=input("Nerede oturuyorsun?")
print(ikamet,"in havasini cok severim. Cok sanslisin.")
sarkici=input("En sevdigin sarkici kim?")
print("Bir defa",sarkici,"nin konserine gitmistim. Cok keyifliydi.")




