    #TASK
                              Exercise 144 

Alphabet Rangoli
You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:

Sample Input

5


Sample Output

--------e--------

------e-d-e------

----e-d-c-d-e----

--e-d-c-b-c-d-e--

e-d-c-b-a-b-c-d-e

--e-d-c-b-c-d-e--

----e-d-c-d-e----

------e-d-e------

--------e--------

        #SOLUTION

num = int(input(""))
alpha = "abcdefghijklmnopqrstuvwxyz"[0:num]
for i in range(num-1, -num, -1):
  x = abs(i)
  satır = alpha[num: x:-1] + alpha[x:num]
  print(x * "--", "-".join(satır), x * "--")

... 5
-------- e --------
------ e-d-e ------
---- e-d-c-d-e ----
-- e-d-c-b-c-d-e --
 e-d-c-b-a-b-c-d-e 
-- e-d-c-b-c-d-e --
---- e-d-c-d-e ----
------ e-d-e ------
-------- e --------


