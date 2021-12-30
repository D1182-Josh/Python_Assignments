    #TASK 

#    Write a Python program to sum of  three given integers. however, if two value are equal sum will be zero.

    #SOLUTION-1

    num =list(map(int, input("").split()))
    if num[0] == num[1] or num[1] == num[2] or num[0] == num[2] :
        print(0)
    else:
        print(sum(num))

     
     #SOLUTION-2

     num1 = (input("birinci sayıyı girin :"))
     num2 = (input("ikinci  sayıyı girin :"))
     num3 = (input("üçüncü sayıyı girin : "))

     if num1 == num2 or num1 == num3 or num2 == num3 :
        print(0)
     else:
        print(num1 + num2 + num3)
    


