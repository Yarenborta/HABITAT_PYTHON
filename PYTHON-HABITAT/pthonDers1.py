print("Merhaba dünya")
print('Merhaba dünya')
#print("Merhaba Arzu') aynı tırnak içinde kapatılmadığı için hata verecektir.
print("5+4")
print (5+4)
print("Hoş geldin","Arzu")
print('merhaba","arzu')
#print('Ankara'dan geldim')her yeri aynı tek tırnak içine aldığımız için hata verecek. yalnzıca ankara yı almış olacak diğer kelimeleri almayacak
print("Havalar soğuk", end=".")# end " " bir . koyacak alttaki cümle ile
print("Ankara'dan geldim")

print("Havalar soğuk", end=" ")# end " " alttaki cümleyi yanına yazar
print("Ankara'dan geldim")

print("Merhaba", "Dünya", end=" \n ")# end " " satır koyacak alttaki cümle ile
print("Havalar soğuk")

#sep kelimelerin arasına içine yazdığın şeyi yazar
print("My name is","Erdal",sep="-")#My name is - Erdal

print("My name is","Erdal",sep="-",end=".")
print("3+5'in sonucu","8'dir", sep="=",end=".")
print("3+5",3+5,sep="=")

print("merhaba","dünya","nasılsın",sep="\n")

print("Yaren","BÖRTA","İzmir",sep="\n")

print('Hasan"Ankara\'dan geldim",dedi',end=".")#\ kaçış karakteri yani yanındaki'yı hata olarak çıktıda göstermedi
print("Hasan","Ankaraya geldi",sep="-",end="\n")
print()#boş bir satır yapar.
print("\n\n\n")#tırnaksız olsaydı hata verir.
# """   """  yaparak da yourm cümlesi olur

isim="Erdal"
yas=45
print(isim)
print(yas)
print("Merhaba"+ isim +"yaşınız:"+ str(yas))
print("Merhaba",isim,"yaşınız:",yas)

#kullanıcıdan bilgi almak istiyorsak INPUT ile alınır
isim=input("lütfen adınızı yazınız: ")
print("merhaba", isim)
"""

"""

isim=input("adınızı yazınız: ")
yas=input("yasınızı girin lütfen: ")
print("merhaba",isim, "yasınız",yas)




      
