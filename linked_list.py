    #TASK

#You are given two non-empty linked list representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself. 
    
    Example : 
        input : 11 = [2, 4, 3], 12 = [5, 6, 4]
        output : [7, 0, 8]


    #SOLUTION

    liste1 = [9,9,9,9,9,9,9,9,9]
liste2 = [9,9,9,9]

str_liste1 = "".join([str(i) for i in liste1[::-1]])
str_liste2= "".join([str(j) for j in liste2[::-1]])

print([int(i) for i in (str(int(str_liste2) + int(str_liste1)))[::-1]])
