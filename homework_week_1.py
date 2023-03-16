#question1

r = int(input("Lütten dairenin yarı çapını cm cinsinden giriniz.. :"))

formul = 3.14 * (r*r)

formul = str(formul)

print("Dairenin alanı", formul ,"cm2'dir.")
print(" "*len("Dairenin alanı"),"-"*len(formul))

#question2

ad = input("Adınızı giriniz. :")
soyad = input("Soyadınız giriniz.")

print("Merhaba", soyad, ad, sep = "   ")




#question3

ad = input("Adınızı giriniz. :")
soyad = input("Soyadınız giriniz. :")
sehir = input("Yaşadığınız şehri giriniz :")
print(ad, soyad, sehir, "*"*len(sehir), sep = "\n" )

#question4

saniye = int(input("Saniye giriniz :"))

print(saniye,"saniye\n" , saniye/86400, "gündür.\n" , saniye / 3600, "saattir.\n", saniye/60,"dakikadır.")


#question5

ad = input("Adınızı giriniz. :")
soyad = input("Soyadınız giriniz. :")

print("|", "*"*(len(ad)+len(soyad)+1), "|", sep = "")
print("|", " "*(len(ad)+len(soyad)+1), "|", sep = "")
print("|", ad," ", soyad, "|" , sep = "")
print("|", " "*(len(ad)+len(soyad)+1), "|", sep = "")
print("|", "*"*(len(ad)+len(soyad)+1), "|", sep = "")



#question6

ad = input("Sohbet etmek için adınızı giriniz. :")
print("Sayın", ad ,"hoşgeldiniz.")

answer1 = input("Nasılsınız ?")
print("bende iyiyim.")

answer2 = int(input("kaç yaşındasınız ?"))
myage = 15
print("Aramızdaki yaş farkı", answer2-myage)

county = input ("Nerelisiniz ?")
print("güzel memleket")

soyad = input("Soyadınız giriniz. :")
print("Soyadınız : ", soyad)
