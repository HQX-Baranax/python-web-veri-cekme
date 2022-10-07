islem = input("işlem seçiniz:")
sayi1 = input("1. sayıyı giriniz: ")
sayi2 = input("2. sayıyı giriniz: ")
if(islem == "+"):
    toplam = int(sayi1)+int(sayi2)
elif(islem=="-"):
    toplam = int(sayi1)-int(sayi2)
elif(islem=="*"):
    toplam = int(sayi1)*int(sayi2)
elif(islem=="/"):
    toplam = int(sayi1)/int(sayi2)
else:
    print("Lütfen İşelem Giriniz (+,-,*,/)")
print(toplam)
