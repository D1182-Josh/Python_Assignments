    #TASK

#   Write a function that inverts the keys and values of a dictionary.
    invert ={"zebra": "koala", "horse":"camel"}
    Output
      {"koala":"zebra","camel":"horse"}


   #SOLUTION1

invert ={ "zebra": "koala", "horse": "camel" }
n_invert = {}

for x, y in invert.items() :
  n_invert[y] = x

print(n_invert)
 
    #SOLUTION2

 invert ={ "zebra": "koala", "horse": "camel" }
dict([(y,x) for x,y in invert.items()])
