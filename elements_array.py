    #TASK

#In this challenge you will be given an array similar to the following : [[3], 4, [2], [5], 1, 6] in words, elements of the array are either an integer or an integer containing a single integer.We humans can clearly see that this array can reasonably be sorted according to "the content of the elements" as : [1, [2], [3], 4, [5], 6] Create a function that, given an array similar to the above , sorts the array according to the " content of the elements". 
    Examples:
         sort([4, 1, 3]) --> [1, 3, 4]
         sort([[4], [1], [3]]) --> [[1], [3], [4]]


    #SOLUTION1

arry = [[3], 4, [2], [5], 1, 6]
n_arry = sorted([arry[i][0] if type(arry[i]) == list else arry[i] for i in range(len(arry))])
for i in range(len(n_arry)) :
    ... [ 1, 2, 3, 4, 5, 6]

    #SOLUTION2
 
def sortIt(arry) :
  n_arry = sorted([arry[i][0] if type(arry[i]) == list else arry[i] for i in range(len(arry))])
  return [[n_arry[i]] if n_arry[i] not in arry else n_arry[i] for i in range(len(arry))]

sortIt([[3], 4, [2], [5], 1, 6])
... [1, [2], [3], 4, [5], 6]


    
