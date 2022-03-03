    #TASK

#Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.
 Examples.
 ["cow", "pig", "cow", "cow"] --> {"cow", "pig"}
 ["table", "table", "table"] --> {"table"}

 #SOLUTION

arry = ["cow", "pig", "cow", "cow"]
plural = []
for i in arry :
  if arry.count(i) > 1 :
    plural += [i + "s"]
  else :
    plural += [i]

arry = ["cow", "pig", "cow", "cow"]
set([i + "s" if arry.count(i) > 1 else i for i in arry]) 
