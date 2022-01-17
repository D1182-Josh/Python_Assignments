    #TASK

#You are given a string. Your task is find out if the string contains: alphanumeric characters, digits, lowercase and uppercase characters.

#ınput format 
#A single line containing a string.

#output format 


#in the first line, print True if has any alphanumeric characters. Otherwise, print False. In the second line, print True if has any alphabetical characters. Otherwisw, print False. ın the third line, print True if has any digits. Otherwise , print False. In the fourth line, prin True if has any lowercase. Otherwise, print False. In the fifth line, print True if has any uppercase characters. Otherwise, print False.

Sample input
qA2

Sample output 
True
True
True
True
True


    #SOLUTION
text = input("")
print(any(i.isalnum() for i in text))
print(any(i.isalpha() for i in text))
print(any(i.isdigit() for i in text))
print(any(i.islower() for i in text))
print(any(i.isupper() for i in text))
    
