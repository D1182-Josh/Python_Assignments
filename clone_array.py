    #TASK

#The Code tab has a code which attempts to  add a clone of an array to itself. There is no error message, but the results are not as expected. Can you fix the code_
    Examples:
         clone([1, 1]) --> [1, 1, [1, 1]]
         clone([1, 2, 3]) --> [1, 2, 3, [1, 2, 3]]
         clone (["x", "y"]) --> ["x", "y"]]

     #SOLUTION1

arry = [1, 1]
(lambda x : x +[x])(arry)
... [1, 1, [1, 1]]

    #SOLUTION2

def clone(arry):
  return (lambda x : x + [x])(arry)
clone([1,1])



