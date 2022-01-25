    #TASK

#Pyhton program to find the factorial of a number is the product of all the integers from 1 to that number.For example, the factorial of 6 is 12345*6=720. Factorial is not defind for negative numbers, and the factorial of zero is one , 0!=1


    #SOLUTION

n = int(input(""))
faktoriyel = 1
if n < 0 :
  print("Lütfen negatif sayı girmeyiniz! ")
elif n == 0 :
  print("0 faktoriyel 1 e eşittir.")
else :
  for i in range(n,0,-1) :
    faktoriyel *= i
    print("{} faktoriyel {} sayısına eşittir.".format(n, faktoriyel))    
