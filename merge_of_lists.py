    #TASK

#Write a Python to create a merged list of tuples from the two listd given.
For Example : 
    input:
        list1=[195,488,142,626,180]
        list2=["New York","Alabama","Hawaii","Vermont","West Virginia"]

     output:

         list3=[(195,'New York'),(488,'Alabama'),(142,'Hawaii'),(626,'Vermont'),(180,'West Virginia')]

   #SOLUTION

list1=[195, 488, 142, 626, 180]
list2=["New York", "Alabama", "Hawaii", "Vermont", "West Virginia"]

new = list(zip(list1, list2))
print(new)

    #SOLUTION

merge_list = []
for i in range(0, len(list1)) :
  merge_list += [(list1[i], list2[i])]

print(merge_list)    
