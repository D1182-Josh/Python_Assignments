    #TASK

#   Create a string of up to 1000 numbers, then create a python code that finds how many 3 digits occur in this string of numbers.

    #SOLUTION

print(len([i for i in range(1,1001) if "3" in str(i)]))    
