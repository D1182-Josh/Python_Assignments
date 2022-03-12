    #TASK

#   Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters. 

    #SOLUTION

s = input("")
"".join([i.upper() for i in s if len([i for i in s[:4] if i.isupper()]) >= 2])    
