    #TASK

#                        
                               
Advanced List Sort

Create a function that takes a list of numbers or strings and returns a list with the items from the original list stored into sublists. Items of the same value should be in the same sublist.

Examples

advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]

advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]

advanced_sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]

Notes

The sublists should be returned in the order of each element's first appearance in the given list.    

    #SOLUTION
def advanced_sort(arry) :
  arry_dict= {}
  for i in arry :
    if i not in arry_dict :
      arry_dict[i] = [i]
    else :
      arry_dict[i] += [i]
  return [i for i in arry_dict.values()]

advanced_sort([5, 4, 5, 5, 4, 3])

... [[5,5,5], [4,4],[3]]






