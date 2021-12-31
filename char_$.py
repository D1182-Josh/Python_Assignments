#  TASK

# Write a Python program to get a string from a given string where all occurrences of its first**** char have changed to '$', except the first ch**ar itself


#SOLUTION

text = input("")
text =text[0] + text[1:].replace(text[0], "$")
text
