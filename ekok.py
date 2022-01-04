    #TASK 

#Kullanıcıdan alınan iki sayının ekokunu bulan program yazınız


    #SOLUTION

sayi1 =int(input("lütfen ilk sayıyı giriniz : "))
sayi2 =int(input("lütfen ikinci sayıyı giriniz : "))
for i in range(1,min(sayi1, sayi2) +1):
    if (sayi1 % i==0) and (sayi2%i ==0):
        ebob = i
print("Ekok = ", (sayi1*sayi2)//ebob)
