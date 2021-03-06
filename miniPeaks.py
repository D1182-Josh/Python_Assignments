    #TASK

#Write a function that returns all the elements in an array that are strictly greater than their adjacent left and right neighbors.
    Examples:
         miniPeaks([4, 5, 2, 1, 4, 9, 7, 2]) --> [5,9]
         //5 has neighbours 4 and 2, both are less than 5.
          miniPeaks([1, 2 ,1 ,1, 3, 2, 5, 4, 4]9 --> [2, 3, 5]
          miniPeaks([1, 2, 3, 4, 5, 6]) --> []

    Notes: 
        Do not count boundary numbers , since they only have one left/right neighbor.
        if no such number sexist, return an empty array

     #SOLUTION


def miniPeaks(arry) :
  return [arry[i] for i in range(1,len(arry)-1) if arry[i] > arry[i-1] and arry[i] > arry[i+1]]

print(miniPeaks([4, 5, 2, 1, 4, 9, 7, 2]))
print(miniPeaks([]))
... [5, 9]
    []

