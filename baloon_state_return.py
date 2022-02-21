    #TASK

#   Once a water balloon pops, is soaks thearea around it. The ground gets drier the further away you travel from the balloon. The affect of a water balloon popping can be modeled using a list. Create a function that takes a list which takes the pre-pop state and retuns the state after the balloon is popped. The pre-pop state will contain at most a single balloon, whose size is represented by the only non-zero element. 

    Examples pop([0, 0, 0, 0, 4, 0, 0, 0, 0,])--> [0, 1, 2, 3, 4, 3, 2, 1, 0]
    pop([0, 0, 0, 3, 0, 0, 0])--> [0, 1, 2, 3, 2, 1, 0]
    pop([0, 0, 2, 0, 0]) --> [0, 1, 2, 1, 0]
    pop([0]) --> [0] Notes Length if input list is always odd. The input list will always be the exact length it takes for there to be exactly one border zero. If the inoput list cocsists only of zeroes, return the same list.

    #SOLUTION

baloon = [0, 0, 0, 0, 4, 0, 0, 0, 0]
max_b = max(baloon)
new_list = []
for i in range(max(baloon)) :
  new_list += [i]
for j in range(max(baloon),-1,-1) :
  new_list += [j]

print(new_list)    
