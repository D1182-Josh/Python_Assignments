    #TASK 

#    Write a Python program to sum of  three given integers. however, if two value are equal sum will be zero.

    #SOLUTION

    num =list(map(int, input("").split()))
    if num[0] == num[1] or num[1] == num[2] or num[0] == num[2] :
        print(0)
    else:
        print(sum(num))
    


