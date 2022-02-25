    #TASK

#Given a list of tuples, implement a methot that sorts the list in ascending order by the second element inside the tuples and retuns the list. 

    Examples:

        input: [('b', 1), ('c', 2), ('x', 3), ('x', 4), ('z', 0)]
        output : [('z', 0), ('b', 1), ('c', 2), ('x', 3), ('x',4)]


    #SOLUTION

liste = [("b",1), ("c", 2), ("x", 3), ("x", 4), ("z", 0)]
sorted(liste, key = lambda x : x[1])    
