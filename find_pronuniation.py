    #TASK

#Write a program that takes a maximum rwo-digit(1-99) number from the user and finds the pronunciation of that number. 
For example: input : 97
             output : Doksan Yedi

    #SOLUTION

sayı = int(input(""))
birler= ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar= ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]

birinci_b = sayı % 10
ikinci_b = sayı // 10
if len(str(sayı)) == 2:
  print(onlar[ikinci_b], birler[birinci_b])
elif len(str(sayı)) == 1 :
  print(birler[birinci_b])    
