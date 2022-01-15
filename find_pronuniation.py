    #TASK

#Write a program that takes a maximum rwo-digit(1-99) number from the user and finds the pronunciation of that number. 
For example: input : 97
             output : Doksan Yedi

    #SOLUTION1

sayı = int(input(""))
birler= ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar= ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]

birinci_b = sayı % 10
ikinci_b = sayı // 10
if len(str(sayı)) == 2:
  print(onlar[ikinci_b], birler[birinci_b])
elif len(str(sayı)) == 1 :
  print(birler[birinci_b])

 #SOLUTION2

num = int(input("Enter your 2-digit number: "))
ones = ["sıfır", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
tens = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
digit_ones = num % 10
digit_tens = num // 10
print(tens[digit_tens], ones[digit_ones])    








