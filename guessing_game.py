    #TASK                            

#Write a pyhton code, which is a number guessing game that tries to find the number that will be randomly selected from the number sequence from 1 to 100.
#and indicate in the code that each user has the right to guess 5, deduct 1 right for each wrong guess     
    #SOLUTION

import random
import time
rastgele = random.randint(1,100)
hak = 5
while True:
    kullanıcı = int(input("sayı giriniz:"))
    if kullanıcı<rastgele:
        time.sleep(2)
        hak -= 1
        print("sayıyı yükselt")
    elif kullanıcı>rastgele:
        time.sleep(2)
        hak -= 1
        print("sayıyı düşür")
    else:
        print("tbr tbr")
        break
    if hak == 0:
        print("hakkınız bitti")
        break    
