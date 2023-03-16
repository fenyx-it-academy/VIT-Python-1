
#cevap1

yaricap=int(input("Dairenin yaricapi:"))
pi=3.14159
alan=pi*(yaricap*yaricap)
uzunluk=len("dairenin alani=   cm2 dir")
print("Dairenin alani", alan,"cm2'dir.", "\n", "-"*uzunluk)



#cevap2

isim=input("Adiniz nedir? ")
soy_isim=input("Soyadiniz nedir? ")
isim,soy_isim=soy_isim,isim
print("Merhaba", isim ,soy_isim, sep="   ")


#cevap3
kartvizit_ad=input("Ad:")
kartvizit_soyad=input("Soyad:")
kartvizit_adres=input("Adres:")
print(kartvizit_ad,kartvizit_soyad,kartvizit_adres, "*" *len(kartvizit_adres), sep="\n")


#cevap4
girilen_saniye=int(input("saniyeyi giriniz:"))
saniye=girilen_saniye%60
dakika=(girilen_saniye//60)%60
saat=(girilen_saniye//60)//60
gun=(saat//24)
print(gun,saat,dakika,saniye, sep=":")

#cevap5
isim=input("Adiniz:")
soy_isim=input("Soyadiniz:")
isimvesoy_isim=(isim+" "+soy_isim).upper()

lenisimvesoy_isim=len(isimvesoy_isim)
print("-"*(lenisimvesoy_isim+5))
print("|" +" "*(lenisimvesoy_isim+2)+"|")
print("|" +""*1,isimvesoy_isim,""*1+"|")
print("|" +" "*(lenisimvesoy_isim+2)+"|")
print("-"*(lenisimvesoy_isim+5))


#cevap6
isim=input("Merhaba,\nisminiz?: ")
print("Hosgeldin ",isim, end=".\n")
hal_hatir=input("Nasilsin?: ")
nick_name=input("Bu senin gercek adin mi yoksa nick name in mi?: ")
print("Hmmm, anladim!")
yas=input("Kac yasindasin?: ")
print("Demek", yas, "yasindasin. Ne guzel!")
hobby=input("Hobilerin neler?: ")
print(hobby, "guzeldir.")
memleket=input("Nerelisin?: ")
print(memleket, "guzel memlekettir.")
print("Tanistigima memnun oldum. Ben kacar.")
