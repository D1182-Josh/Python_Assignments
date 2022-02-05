    #TASK

#Write a program that square every digit of a number and concatenate them.For Example: if we run 9119 through the function, 811181 will come out, because 82 is 81 and 12 is 1.

    #SOLUTION

num  = input("")
print("".join([str(i) for i in [int(i) ** 2 for i in num]]))    
