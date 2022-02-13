    #TASK

#   You are given an m x n integer grid where accounts[i][j  is the amount of money the its customer has in the jth bank. Return the wealth that richest customer has. A customer's wealth is the amount of money have in all their bank accounts. The richest customer is the customer that has the maximum wealth. 
    
    Example: 
        Input: accounts = [[1,2, 3], [3,2,1]]
        Output: 6
       
    Explanation: 
        1st customer has wealth= 1 + 2 + 3 = 6
        2nd customer wealth = 3 + 2 + 1= 6
        Both customer are considered the richest with a wealth of 6 each , so return 6. 



   #SOLUTION

accounts = [[1,2,3],[3,2,1]]

richest = []
for i in accounts :
  richest += [sum(i)]
print((max(richest)))    
