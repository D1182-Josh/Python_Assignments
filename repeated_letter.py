    #TASK

#Write a program that shows which letter is used how many times in the text received from user.

    #SOLUTION

text = input("")
dict_text = {}
for i in text :
  if i not in dict_text :
    dict_text[i] = 1
  else :
    dict_text[i] += 1    
