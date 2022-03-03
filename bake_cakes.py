    #TASK

#Pete likes to bake some cakes. He has some recipes and ingredients. Unfotunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes? Write a function cakes(), which takes the recipe (object) and the avaible ingredients (also an object) and returns the maximum number of cakes pete can bake (integer). For simplecity there are no units for yhe amounts (e.g 1 lb of flour or 200 g of sugar are simply 1 or 200). ıngredients that are not present in the objects, can be considered as 0.
 
 Examples:
     must return 2
     cakes({flour: 500, sugar: 200, eggs:1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})

     must return 0
     cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour:2000, milk: 2000})

     #SOLUTION1

cake  = {"flour" : 500, "sugar": 200, "eggs": 1}
ingredients =  {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
malzeme = []

for i in cake.keys() :
  if i not in ingredients.keys() :
    print(0)
    break
else :
  for i in list(zip(cake.values(), ingredients.values())) :
    malzeme += [i[1] // i[0]]
  print(min(malzeme))

    #SOLUTION2

cake = {"flour" : 500, "sugar": 200, "eggs": 1}
have = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
new_cake = []

for i,j in cake.items():
  new_cake.append(have.get(i,0)//j)
print(min(new_cake))




