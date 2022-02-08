    #TASK

#Given an integer n, return true if it is a power of two. Otherwise, return false. An integer n is a power of two, if there exists an integer x such that n==2x.

    Example:
        Input: n=1
        Output: true
        Explanation: 2⁰=1


   #SOLUTION1

n = int(input(""))
n_list = []
for i in range(2,n+1) :
  if n % i == 0 :
    n_list += [i]
all([i % 2 == 0 for i in n_list])

    #SOLUTION2

x = 1 
for i in range(x) :
  if 2 ** i == x :
    print(True)
    break
else:
  print(False)    
