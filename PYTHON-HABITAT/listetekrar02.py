
####          L I S T    T E K R A R

dizi1=[1,2,3]
dizi2=[4.0,5.7,4.5]
dizi3=["a","b","c"]
dizi=[dizi1,dizi2,dizi3]
##

dizi=["elma","armut","portakal","mandalina"]
cikti=dizi[1:3]
cikti=dizi[:3]
print(cikti)
##

dizi=["a","b","c","d","e","f","g","h"]
cikti=dizi[5:]
print(cikti)
##

dizi=["a","b","c","d","e","f","g","h"]
cikti=dizi[len(dizi)-1] #yani cikti=dizi[7] diiznin 7. elemanını soruyor.
cikti=dizi[len(dizi)+1] # 9.indisimiz yok. bu yüzden hata verir.
cikti=dizi[len(dizi)-1:0:-4] # sondakinden 0'ya kadar ama 4'er 4'er atla.
print(cikti)
##

dizi1=["a","b","c","d"]
cikti=dizi1+["e"]
print(cikti)
##

dizi1=["a","b","c","d"]
# dizi1[3]="x"
# dizi1[4]="x" # 4, indis dışında olduğu için IndexError verir.   
# cikti=dizi1
# print(cikti)
cikti=dizi1+["z"]
cikti=str(dizi1)+"z" #['a', 'b', 'c', 'd']z çıktısı verir.
# cikti[4]="w" # ["w"] deseydik dizi1 listesinin içine [w] liste atadık yani liste içine liste
print(cikti)
##

dizi1=["a","b","c","d","e"]
dizi1[1:4]=["x","y","z"]
cikti=dizi1
print(cikti)
##

dizi1=["a","b"]
dizi1=dizi1*10
print(dizi1)
##

dizi=["a","b"]
dizi.append("c")
dizi.append("c")
print(dizi)
##

kume={1,2,3,4} # Kümede eleman tekrarı yok. aynı şeyi birden fazla yazdırmaz
kume.add(4)
kume.add(4)
print(kume)
##

dizi=["a","b","a","b","a","c"]
say=dizi.count("a")
print(say)
##

dizi=["a","b","c"]
dizi.insert(1,"x")
print(dizi)
##

a= "     Habitat - Python!     "
print(a.strip()) # Baştaki ve sondaki boşlukları siler/görmemezlikten gelir.
##

a="Ankara,Kayseri,Nevşehir, Kırşehir,İç Anadolu bölgesindedir"
print(a.split("a")) # a gördüğü yerde onu yok sayıp ayır.
##

a="Habitat ile Python"
print(a.upper()) #hepsini büyülterek yazar
print(a.lower()) #hepsini küçülterek yazar
##

a="Muz sevilen bir  meyvedir"
print(a.replace("Muz","çilek")) # Muz gördüğümüz yere çilek yaz
##

a="Ankara,Edirne,Malatya,Bolu,Bursa,İzmir"
b=a.replace(",","-")
print(b)
##

txt="Sevdiğim havalar yağmurlu havalardır."
x="mur" in txt # "mur" txt içinde yer alıyor/içinde
print(x) #True
x="mur" not in txt # "mur" txt içinde yok/ yer almıyor
print(x) #False
##

metin="Bugünlerde \"Outliners\" kitabını okuyorum" 
metin='Bugünlerde "Outliners" kitabını okuyorum'
metin="Bugünlerde 'Outliners' kitabını okuyorum"
metin="Bugünlerde 'Outliners' kitabını okuyorum"
print(metin)
print(" \" Bugünlerde 'Outliners' kitabını okuyorum \"  ")
##





