    #TASK

#   Write a program , persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit. 

    persistence(39) # returns 3 , because 3*9=27, 2*7=14, 1*4=4
                    #and 4 has only one digit

    persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                     # 1*2*6=12, and finaly 1*2=2
            
    persistence(4) # returns 0, because 4 is already a one-digit number



    #SOLUTION

num = input("")
toplam = 1
count = 0

if len(num) == 1 :
  print(count)
else :
  while len(num) != 1 :
    count += 1
    for i in num :
      toplam *= int(i)
    if len(str(toplam)) == 1 :
      print(toplam)
      break
    else :
      num = str(toplam)
      toplam = 1

print(count)    
