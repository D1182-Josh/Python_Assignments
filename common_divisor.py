     #TASK

     Write a program that prints the common divisors of two numbers.



     #SOLUTION

    num1 = int(input("please enter first number :"))
num2 = int(input("please enter second number :"))
toplam = []

    for i in range(1,num1+1) :
     if num1 % i == 0:
       toplam += [i]
       num1 = num1 // i
    for j in range(1,num2+1) :
     if num2 % j == 0:
       toplam += [j]
       num2 = num2 // j
    print(set(toplam))
