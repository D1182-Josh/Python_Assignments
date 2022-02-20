    #TASK

#   Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string. For Example, if given the input 'stress', the function should retun 't'i since the letter t only occurs once in the string, and occurs first in the string. As an added challange, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'. If a string contains all repeating characters, it should return an empty string("") or None -- see sample tests. 

    #SOLUTION1

letter = input("")

for i in letter :
  if letter.count(i) == 1 :
    print(i)
    break
else :
  print(None)

  #SOLUTION2


letter = input("") #sTreSS
lower_letter = letter.lower() #stress

for i in lower_letter :
  if lower_letter.count(i) == 1 :
    print(letter[lower_letter.index(i)])
    break
else:
  print(None)  
