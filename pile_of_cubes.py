	#TASK
#	Mubashir needs your help to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of n^3, the cube above will have volume of (n-1)^3 and so on until the top which have a volume of 1^3.
#Given the total volume  m of the building ,  can you find the number of cubes n required for the building? 
#	In other words, you have to retun an integer b such that: 
#	n^3 +(n-1)^3 + ....+1^3 == m
#	Return None if there is no such number.
#	Examples
#	pile_of_cubes(1071225) --> 45
	pile_of_cubes(4183059834009) --> 2022
	pile_of_cubes(16) --> None

	#SOLUTION1
num = int(input(""))
cube , total = 0 , 0
while total < num :
  cube += 1
  total += cube ** 3

print(cube if total == num else None)

    #SOLUTION2
def find_nb(m):
    total = 0
    n = 0
    
    while (total < m):
        n = n + 1
        total = total + n ** 3
        
    return n if total == m else -1
    
find_nb(1071225)    
