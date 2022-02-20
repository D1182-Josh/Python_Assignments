    #TASK

#   Abigail and Benson are playing Rock, Paper, Scissors, Each game is represented by an array of length 2, where the first element represents what Abigail played and the second element represents what Benson played. Given a squence of game, determine who wins the most number of matches. If they tie, output "Tie". 
    # R stands for Rock
    #P stands for Paper
    #S stands for Scissors 
    # """

#   x = [["R", "P"], ["R", "S"], ["S", "P"]]

    #SOLUTION

x = [["R", "P"], ["R", "S"], ["S", "P"]]
winner = []

for i in x :
  if i[0] == i[-1] :
    print("Draw!")
  elif (i[0] == "R") and (i[-1] == "S") :
    print("Rock beat Scissors")
    winner += [1]
  elif i[0] == "R" and i[-1] == "P" :
    print("Paper beat Rock")
    winner += [-1]
  elif i[0] == "S" and i[-1] == "P" :
    print("Scissors beat Paper")
    winner += [1]
  elif i[0] =="S" and i[-1] == "R" :
    print("Rock beat Scissors") 
    winner += [-1]
  elif i[0] == "P" and i[-1] =="R" :
    print("Paper beat Rock")
    winner += [1]
  elif i[0] == "P" and i[-1] == "S" :
    print("Scissors beat Paper")
    winner += [-1]

if sum(winner) == 0 :
  print("Tie")
elif sum(winner) >= 1 :
  print("The winner is Abigail")
else:
  print("The winner is Benson") 

