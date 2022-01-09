    #TASK

#Write a python function that takes a positive integer and returns the sum of the cube of all the positive integers smoller than the specified number.

    #SOLUTION

num = int(input(""))
print(sum([i ** 3 for i in range(num)]))    
