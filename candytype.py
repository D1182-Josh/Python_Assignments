    #TASK

#  Alice has candies, where the iᵗʰ candy is of type candyType[i]. Alice noticed she started to gain weight, so she visited a doctor. The doctor advised Alice to only eat n/2 of candies she has(n is alqays even.). Alice likes her candies very much, and she wants to eat the maximum number of different types od candies while still following the doctors's advice. Given the integer array candyType of length n, return the maximum number of different types od candies she can eat is she only eats n-2 of them. 

        Example :
             Input: candyType=[1,1,2,2,3,3]
             Output: 3
           Explanation: Alice can only eat 6/2=3 candies. Since there are only 3 types, she can eat one of each type.


        #SOLUTION

candyType = [6,6,6,6,1,2]
len(candyType) / 2
if len(set(candyType)) == len(candyType) / 2:
  print(len(set(candyType)))
elif len(candyType) / 2 > len(set(candyType)) :
  print(len(set(candyType)))
else:
  print(len(candyType) / 2)        
