    #TASK

#İN THİS EXAMPLE YOU HAVE TO VALİDATE İF A USER input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that. The string has the following conditions to be alphanumeric: 
At least one character("" in not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9 
No whitespaces / underscore

    #SOLUTION

def alphanum(text) :
  return text.isalnum()

alphanum("Clarus way010")
... False
