    #TASK

#Write a python program to test whether all numbers of a list is greater than a certain number

    #SOLUTION

lista = list(map(int, input("").split()))
number = int(input(""))
print(all([i > number for i in lista]))    
