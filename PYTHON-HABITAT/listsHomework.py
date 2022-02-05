
#### LIST HOMEWORK

# 1- listem=[0,1,2,3,4,5,6,7,8,9]
#     a) Bu listedeki tek sayıları bulan kodlar
#     b) Bu listedeki tek sayıları ve çift sayıları ayrı birer listeye yazan kodlar
# Tek sayı yazdırma
listem=[0,1,2,3,4,5,6,7,8,9]
for sayi in listem:
    if sayi %2 !=0:
        print(sayi)
        sayi+=1

# #Çift sayı yazdırma
listem=[0,1,2,3,4,5,6,7,8,9]
for sayi in listem:
    if sayi %2 !=0:
        sayi+=1
        print(sayi)

## ya da;
listem=[0,1,2,3,4,5,6,7,8,9]
print("çiftsayılar:",listem[0:10:2])
print("teksayılar:",listem[1:10:2])
## ya da;
tekListe=[]
ciftListe=[]
listem=[0,1,2,3,4,5,6,7,8,9]
for i in listem:
    if i%2==0:
        ciftListe.append(i)
    else:
        tekListe.append(i)
print("Tek sayılar",tekListe)
print("Çift sayılar",ciftListe)

        
# ÖRNEK 2:
# hafta_ici=["Pazartesi","Salı","Çarşamba","Perşembe","Cuma"]
# hafta_sonu=["Cumartesi","Pazar"]
# a) Bu iki listeyi "APPEND" metodu ile birleştirin
# b) Bu iki listeyi "EXTEND" metodu ile birleştirin

hafta_ici=["Pazartesi","Salı","Çarşamba","Perşembe","Cuma"]
hafta_sonu=["Cumartesi","Pazar"]
hafta_ici.append(hafta_sonu)
print(hafta_ici)
##
hafta_ici.extend(hafta_sonu)
print(hafta_ici)

#ÖRNEK 3:
# 1 ile 20 arasındaki tam sayılardan oluşan bir liste üretin
# a) Bu listedeki ilk 10 sayıyı görüntüleyin
# b) Bu listedeki son 10 sayıyı görüntüleyin

# İlk 10 sayıyı görüntülemek için;
for sayi in range(1,21):   
    if sayi<10:
        sayi+=1 # if'ten önce yazsak da çıktı yine aynı oluyor.
        print(sayi)

## Son 10 sayıyı görüntülemek için;   
for sayi in range(1,21):  
    sayi+=1  
    if sayi>10 and sayi<21:
        #sayi+=1 i buraya yazınca 11'i alamdan yazdırmaya başlıyor ama if'in üstünde yazdırınca 11'i de dahil ederek saymaya başlıyor
        print(sayi)  

# ## ya da ;
numbers=list(range(1,21))
print(numbers)
print(numbers[0:10])
print(numbers[10:21])
## 

# Örnek 4: Kullanıcıdan sayı sayı istenecektir:
# 	Ancak; kullanıcı negatif sayı girince kullanıcıdan artık sayı istemeyecek
# 		En fazla 10 tane sayı girilebilecek
# 		Kullanıcının girdiği sayılar bir listeye aktarılacak 
# 		Kaç tane sayı girildiği yazdırılacak
# 		Sayılar küçükten büyüğe yazdırılacak.



tekrar=0

while tekrar<11:
    number=int(input("Bir sayı giriniz"))
    tekrar+=1
    if tekrar==10:
        print("tekrar bitmiştir")
        break
    elif number<0:
        print(number,"Negatif bir sayıdır. Lütfen geçerli bir değer giriniz.{} defa sayı tekrar edilmiştir".format(tekrar))  
        break


 ### ya da;
 
myList=[]
while True: # sürekli çalış demek, break komutunu gördüğü anda durdurur
    sayi=int(input("Sayı gir:"))
    if sayi<0 or len(myList)>10:
        break
    else:
        myList.append(sayi)
myList.sort()
print("Liste: ",myList,"eleman sayısı: ",len(myList))

#Tek sayıları bir listeye, çift sayı ları ayrı bir listeye alsın.en fazla 10 sayı  girilsin
tek_sayi=[]
cift_sayi=[]
liste=0
while liste<10:
    liste+=1
    sayi=int(input("Sayı gir:"))
    if liste%2==0:
      cift_sayi.append(liste)
    else:
        tek_sayi.append(liste)
print(tek_sayi,cift_sayi)

cift=[]
tek=[]
a=0
while a<10:
    sayi=int(input("sayi gir"))
    if sayi%2==0:
        cift.append(sayi)
        break # çift sayı gelene kadar çalışır
    else:
         tek.append(sayi)
print(cift)
print(tek)
##

meyveler=["Elma","Armut","Muz"]
sebzeler=["Patates","Oğan","Ispanak"]
gida=["Çay","Şeker"]
listem=[meyveler,sebzeler,gida]
# listem.append(meyveler)
# listem.append(sebzeler)
# listem.append(gida)
print(listem[0]) # print(listem[0][1])
#print(len(listem))
##
sepet={"elma":5,"armut":4,"muz":10}
print(sepet["elma"])
##

a="Arzu,Erdal,Mustfa,Ahmet,Ali"
ogrenciler=[]
ogrenciler=a.split(",") # a daki her bir elemenaı ayrı ayrı alır.
# # eğer ogrenciler.append(a) dersek bir bütün eleman olarak alır.
print(len(ogrenciler))
##

a="Arzu,Erdal,Mustfa,Ahmet,Ali"
notlar=[60,70,80,90,100]
ogrenciler=a.split(",") #öğrencilerin ilk elemanını alıp notların ilk elemannı ile eşeleştiricez
karne=dict() # boş bir dict. oluşturduk.
for i in range(5): # a da 5 isim olduğu için range(5) yaptık.
    karne[ogrenciler[i]]=notlar[i]
print(karne)
##


##
# Örnek 5:
# ogrenciNotlari={"Arzu":70,"Erdal":35,"Sumeyra":80,"Dua":90,"Meryem":100,"Yaren":75}
# Bu sözlüğe(dictionary) kendi isminizi ve notunuzu ekleyin.
# Kendi isminizin aldığı notu ekrana görüntüleyin

ogrenciNotlari={"Arzu":70,"Erdal":35,"Sumeyra":80,"Dua":90,"Meryem":100,"Yaren":75}
name=input("Lütfen isminizi giriniz: ")
sinav_notu=int(input("Sınav notunuzu yazınız: "))
ogrenciNotlari[name]=sinav_notu
print(ogrenciNotlari)

##

# Örnek 6: notlar={"erdal":{"Mat":45,"Eng":78,"Phys":78,"Science":77},"arzu":{"Mat":45,"Eng":78,"Phys":78,"Science":77}}
# Bu sözlükte “erdal”’ın “Mat” notunu yazdırın.
# notlar["erdal"]["Mat"]
# notlar["arzu"]["Eng"]

notlar={"erdal":{"Mat":45,"Eng":78,"Phys":78,"Science":77},"arzu":{"Mat":45,"Eng":78,"Phys":78,"Science":77}}
print(notlar["erdal"]["Mat"])


ogrenciNotlari={"Arzu":90,"Erdal":60,"Sumeyra":70,"Dua":90,"Meryem":100,"Yaren":90}
top=0
for i,j in ogrenciNotlari.items():
    print("Öğrenci Adı: {0}\t Notu :{1}".format(i,j))
    top+=j
print("Ortalama :{}".format(top/len(ogrenciNotlari)))


notlar={"erdal":{"Mat":45,"Eng":78,"Phys":78,"Science":77},"arzu":{"Mat":45,"Eng":78,"Phys":78,"Science":77}}


y=[]
for i in range(10):
    x=input("enter a no")
    if int(x)<0:
        print("it isn't acceptable")
    else:
        y.append(int(x))
print("The entered numbers are:",y,"and they are:",len(y))
y.sort()
print("Ordered numbers:",y)


