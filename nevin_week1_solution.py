cevap1
#dairenin alanını hesapliyoruz
yaricap=int(input("Dairenin yaricapini giriniz:"))
pi = 3.14 
alan = pi * (yaricap * yaricap) 
baslik=("Dairenin alani:")
print("Dairenin alani:", alan,"cm2'dir","\n","-"*len(baslik),sep="")
cevap2
#kullanicidan ad,soyad alip,selamlama hitabi yazdiriyoruz
#ad soyad yerdegistiriyor aralarinda 3 adet bosluk yazdiriyoruz.
ad=input("Adinizi giriniz:")
soyad=input("Soyadinizi giriniz:")
print("Welcome",soyad,ad,sep="   ")
cevap3
#kisinin ad soyad ve adresini alip altalta yazdiriyoruz
#adresin altina adres kadar * ekliyoruz
ad=input("Adinizi giriniz:")
soyad=input("Soyadinizi giriniz:")
adres=input("Adresinizi giriniz:")
print(ad,soyad,adres,"*"*len(adres),sep="\n")
cevap4
#Girilen saniye degerini saniye,dakika,saat,gun olarak yazdiriyoruz
girilen_saniye=int(input("Saniyeyi giriniz:"))
saniye=girilen_saniye%60
dakika=(girilen_saniye//60)%60
saat=(girilen_saniye//60)//60
gun=saat//24
print("Girdiginiz saniye: ",girilen_saniye,gun,saat,dakika,saniye,sep=":")
cevap5
#Kullanicidan ismini ve soy ismini alip bir dikdortgenin ortasina yazidiriyoruz
#Isim ve Soysisim uzunluguna gore dikdortgen buyuyup kuculuyor
ad=input("Adinizi giriniz:")
soyad=input("Soyadinizi giriniz:")
uzun=len(ad)+len(soyad)+1
yatay=len(ad)+len(soyad)+5
print("-"*yatay,sep="")
print("|"," "*uzun,"|",)
print("|",ad,soyad,"|")
print("|"," "*uzun,"|",)
print("-"*yatay,sep="")
cevap6
#Kullaniciya en az 6 soru sorup, cevaplara gore yanitlar veren basit bir chat programi
print("Hosgeldiniz oncelikle sizi tanimak istiyorum.")
ad_soyad=input("Adiniz - Soyadiniz :")
print("Sizinle tanistigima memnun oldum",ad_soyad)
yas=input("Kac yasindasiniz:")
print(yas,"omrun en guzel caglari")
evhay=input("Hayvanlari sever misiniz? :(E/H)").upper()
if evhay =="E":
    cinsi=input("Ev hayvaniniz var mi  varsa cinsi ?):")
    print("Bir",cinsi,"dostunuz var.")
else:
    input("Hayvanlardan korkuyormusun?")
    print("Bende")
hoby=input("Hobyleriniz?")
print("Benim hobimde",hoby)
input("Calisiyor musunuz yoksa ogrencimisiniz? :")
print("Bu harika")
