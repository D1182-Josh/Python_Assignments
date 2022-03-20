    #TASK

#Last Digit Ultimate :  Your job is to create a function, that takes 3 numbers : a, b, c, and returns True if the last digit of a*b = the last digit of c. Check the examples below for an explanation. 
    Examples: 
        last_dig(25, 21, 125) --> True
#The last digit of 25 is 5, the last digit of 21 is 1, and the last digit of 125 is 5, and the last digit of 5*1 = 5, which is equal to the last digit of 125(5). 
    
        last_dig(55, 226, 5190) --> True
#The last digit of 55 is 5, the last digit of 226 is 6, and the last digit of 5190 is 0, and the last digit of 5*6 = 30 is 0, which is equal to the last digit of 5190(0). 


    #SOLUTION

def last_dig(a,b,c) :
  return str(int(str(a)[-1] ) * int(str(b)[-1]) )[-1] == str(c)[-1]

last_dig(55,226,5190)
... True

