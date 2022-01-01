  # TASK 
  # Create triangle in different formats usingbnumbers.


  #SOLUTION1

# *****
# ****
# ***
# **
# *
for i in range(5,0,-1):
  print(i * "*")

  #SOLUTION2

# 1
# 1 2
# 1 2 3
# 1 2 3 4

num = 5
for i in range(num) :
  for j in range(1, i+1):
    print(j, end = " ")
  print()



  #SOLUTION3

num = int(input(""))
space = (2 * num) - 2
for i in range(num) :
    print(" " * space + (i+1) * "* ")
    space -= 2

  #SOLUTION4

#      1 
#     1 2 
#    1 2 3 
#   1 2 3 4 
#  1 2 3 4 5
num = int(input(""))
for i in range(1,num+1) :
  print(" " * (num +1 -i), *range(1,i+1))  



