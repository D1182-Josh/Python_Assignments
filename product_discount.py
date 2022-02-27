    #TASK

 #Aretailer is having a store-wide "buy 2, get 1 free" sale. For legal reasons, they can't charge their customer $0 for an article so a discount is applied to all products instead. For example, if a customer gets three products a , b and c: 
 Product A $15.99
 Product B $23.50
 Product C $10.75
She gets the cheapest one for free, so she ends up paying $15.99 + $23.50 = $39.49 , but what her receipt says is: 
 Product A $15.99-special discount= $12.57
 Product B $23.50-special discount=$18.47
 Product C $10.75-special discount = $8.45
 Total: $39.49
 
#Create a function that takes in a list of prices for a customer's shopping cart and retuns the prices with the discount applied. Round all prices to the cent.

    #SOLUTION

store = [5.75, 14.99, 36.83, 12.15, 25.30, 5.75, 5.75, 5.75]
sort_list = sorted(store)
indirim_oranı = round((sum(sort_list[:len(store) // 3]) * 100 ) / sum(store) ,2)
print(len(sort_list) // 3)

sort_list
indirim_oranı = round((sum(sort_list[: len(store) // 3]) * 100 ) / sum(store) , 2 )
new_store = []
for i in store :
  new_store.append(round(i - ((i * indirim_oranı) / 100),2))

new_store    


    #SOLUTION

[round(i,2) for i in list(map(lambda x : x - (x * indirim_oranı) / 100 , store))]
[2.99, 5.75, 3.35, 4.99]

store = [10.75, 11.68]
sort_list = sorted(store)
indirim_oranı = round((sum(sort_list[:len(store) // 3]) * 100 ) / sum(store) ,2)

[round(i,2) for i in list(map(lambda x : x - (x * indirim_oranı) / 100 , store))]








