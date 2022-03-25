    #TASK
# A friend of mine takes the squence of all numbers from 1 to n (where n > 0). Within taht squence, he chooses two numbers, a and b. He says taht the product of a and b should be equal to the sum of all numbers in the squence, excluding a and b. Given a number n, could you tell me the numbers he excluded from the squence? The function takes the parameter: n ( n is always strictly greater than 0) and returns an array or a string (depending on the language) of the form:
    [(a,b, ...] or [[a,b], ...] or {{a,b}, ...} or [{a,b}, ...]
#with all (a,b) which are the possible removed numbers in the squence 1 to n. [(a,b), ...] or  [(a,b, ...] or [[a,b], ...]  [(a,b, ...] or ....
#It happens that rhere are several possible (a,b). The function returns an empty array (or an empty string) if no possible numbers are found which prove that my friend has not told the truth! 
    Examples:
        removeNb(26) should return [(15,21), (21,15)]
        or 
        removeNb(26) shoud return {{15,21}, {21,15}}
        or 
        removeNb(26) should return [[15,21],[21,15]]
        or 
        removeNb(26) should return [{15,21},{21,15}]
        or 
        removeNb(26) should return "15 21, 21 15"
        in C:
# removeNb(26) should return {{15,21}{21,15}} tested by way of string. Function removeNb should return a pointer to an allocatedarray of  Pair  pointer, each one also allocated.

    #SOLUTION

def removeNb(num) :
  return [[i,j] for i in range(1,num+1) for j in range(1,num+1) if i * j  == sum([i for i in range(1,num + 1)]) - i - j]

removeNb(26)
 ... [[15, 21], [21,15]]

