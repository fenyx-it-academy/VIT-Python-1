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


