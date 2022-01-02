    #TASK

# Write a python program to get a string made of the first 2 and the last 2 chars from a given a string.If the string length is less than 2, return instead of the empty string.


    #SOLUTION
 
text = input("")
if len(text) < 2 :
  word = "Empty String"
else :
  word = text[0:2] + text[-2:]
print(word) 
