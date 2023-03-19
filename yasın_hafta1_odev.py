#ODEV1
#Kullanicidan yari cap isteyip dairenin alanini hesaplayalim
#Pi sayisini 3 olarak aldim

yaricap=input("Dairenin Yari capini giriniz:")
Alan= str(int(3 * int(yaricap) * int(yaricap)))
print("Dairenin alani " + str (Alan) + " cm2 ")
print("-" *(20 + len(Alan)))

#Ad soyad ve adresi kullanicidan alip bunlari yazdiracagim/
#Ad ve soyadin yerleri deisip aralarinda 3 bosluk olacak/
#ODEV2
Adi=input("Adiniz Nedir?")
Soyadi=input("Soyadiniz Nedir?")
print("Merhaba", Soyadi + "   " +Adi)


#ODEV3
#Kisinin adini soyadini ve adresini alip yazdiracagiz.
#adresin altinda adres kadar yildiz olacak
ad=input("Kisinin adi:")
soyad=input("Kisinin Soyadi:")
adres=input("Kisinin adresi:")
print(ad,soyad,adres, "*"* len(adres), sep="\n")


#ODEV4
# Kuulanicidan saniye alip saniye, dakika, saat ve gun olarak yazdiracagiz.
saniye=int(input("Saniyeyi girin:"))
dakika=int(saniye/60)
saat=int(dakika/60)
gun=int(saat/24)
print(str(gun) + " gun ", str(saat) + " saat ", str(dakika) + " dakika ",str(saniye) + " saniye ", sep="\n")


#ODEV5
#Adimizi ve soyadimizi ayni kullanicidan aldik ve
# bunlari bir dikdorgenin icine gelecek sekilde yazdirdik
ad_soyad=input("adinizi ve soyadinizi girin:")
print("I","*"*(len(ad_soyad)+2),"I",sep="")
print("I"," "*(len(ad_soyad)),"I")
print("I",ad_soyad,"I")
print("I"," "*(len(ad_soyad)),"I")
print("I","*"*(len(ad_soyad)+2),"I",sep="")


#ODEV6
#Kisa bir sohbet konusmasi yazacagim. Sordugum sorulara uygun cevap almak istiyorum.
ad=input("Merhaba, adin ne?",)
print("Sana da merhaba " +ad+ ",benim adim da Ali.")
yas=input("Kac yasindasin " +ad+ "?")
print("Sanki daha yasli gibisin"+"!!!")
memleket=input(ad+" memleket neresi?")
print("Ooooooo " + memleket + " mi," + " orayi iyi bilirim" +  ". Birkac ay orada yasadim.")
ev=input(ad+ " simdi nerede oturuyorsun?")
print( ev + " demek. Orayi hic gormedim ama " + " guzel bir yer oldugunu dusunuyorum.")
yil=input("Kac yildir orada oturuyorsun?")
print(yil+ " yil" + " bence baya uzun bir zaman.")
hobi=input("Hobilerin neler?")
print(hobi + " bunlar eglenceli ve guzel hobiler. Seni tebrik ederim.")
print("Benden bir istegin var mi "+ ad + "? Benim gitmem gerekiyor. Kendine iyi bak!!!")








 

