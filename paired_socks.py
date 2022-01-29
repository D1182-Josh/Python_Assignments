    #TASK

#There a large pile of socks yhat must be paired bu color. Given an array of integers representing the color of each of sock, determine how pairs of socks with matching colors there are. 

#Example 
    
#    n = 7
#    ar = [1,2,1,2,1,3,2]
#    There is one pair of color and one of color 2. There are three odd socks left , one of each color. The number of pairs is 2. 

    #SOLUTION

socks = list(map(int, input("").split()))
socks_dict = {}
for i in set(socks) :
  socks_dict[i] = socks.count(i)

pairs = 0
for j in socks_dict.values() :
  pairs += j // 2
print(pairs)    
