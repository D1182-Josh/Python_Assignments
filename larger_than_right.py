    #TASK

# Create a function that retrieves every number that is strictly larger than every nymber that follows it. 
    Examples :
        larger_than_right([3, 13, 11, 2, 1, 9, 5]) --> [13, 11, 9, 5]
        13 is larger than all numbers to its right, etc.
    Must be strictly larger. Always include the last number. 
    larger_than_right([5, 5, 5, 5, 5,5]) --> [5]
    larger_than_right([5, 9, 8, 7]) --> [9, 8, 7]
    Notes
    The last number in an array is trivially strictly  larger than all numbers that follow it (no numbers follow it).


    #SOLUTION1

arry = [3, 13, 11, 2, 1, 9, 5]
# output [13, 11, 9, 5]
n_arry = []
for i in  range(0,len(arry)-1) :
  if all([arry[i] > j for j in arry[i+1:]]) == True :
    n_arry += [arry[i]]

n_arry + [arry[-1]]

    #SOLUTION2

    

    
