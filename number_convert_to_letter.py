    #TASK

#Write a python code that converts the number between 0 and 999 to letter and tells me

    #SOLUTION

num = int(input("Enter your number: "))
ones = ["sıfır", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
tens = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
hundred = ["", "yüz", "iki yüz", "üç yüz", "dört yüz", "beş yüz", "altı yüz", "yedi yüz", "sekiz yüz", "dokuz yüz"]

digit_hundred = (num % 1000 - num % 100) // 100
digit_tens = (num % 100 -num % 10 ) // 10
digit_ones = num % 10


if len(str(num)) == 1 :
  print(ones[digit_ones])
elif len(str(num)) == 2 :
  if str(num).endswith("0"):
    print(tens[digit_tens])
  else :
    print(tens[digit_tens], ones[digit_ones])
elif len(str(num)) == 3 :
  if str(num).endswith("0") :
    print(hundred[digit_hundred],tens[digit_tens])
  else :
     print(hundred[digit_hundred],tens[digit_tens], ones[digit_ones])    
