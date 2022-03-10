    #TASK

#Complete function that :
#       1.accepts two integer arrays of equal length 
#       2. compares the value each member in one array to the corresponding member in the other.
#       3. squares the absolute value difference between those values and returns the average of those squared absolute value diffrence between each member pair
 
 #  Examples 
        [1, 2, 3], [4, 5, 6] --> 9 because (9 + 9 + 9) / 3 
        [10, 20, 10, 2], [10, 25, 5, -2] --> 16.5 because (0 + 25 + 25 + 16) /4
        [-1, 0], [0, -1] --> 1 because (1+1) /2


      #SOLUTION

arry1 = [10,20,10,2]
arry2 = [10,25,5,-2]

print(sum([(arry2[i] - arry1[i]) ** 2 for i in range(len(arry1))]) / len(arry1))
        
