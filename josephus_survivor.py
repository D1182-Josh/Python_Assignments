    #TASK

# in this kata you have to  correctly return who is the "survivor", ie: the last element of a josephus permutation. Basically you have to assume that n people are put into a circle and they eliminated in steps of k elements, lekie this: josephus_survivor(7,3) => means 7 people in a circle; one every 3 is eliminated until one remains
    [1,2,3,4,5,6,7] - initial sequence
    [1,2,4,5,6,7] => 3is counted out 
    [1,2,4,5,7] => 6 is counted out 
    [1,4,5,7] => 2 is counted out
    [1,4,5] => 7 is counted out 
    [1,4] => 5 is counted out
    [4] => 1 is counted out, 4 is the last element - the survivor

    #SOLUTION1

liste = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
indeks = 0
uzunluk = len(liste)
while len(liste) > 0 :
  indeks = (2 + indeks) % uzunluk
  liste.pop(indeks)
  print(liste)
  uzunluk -= 1

    #SOLUTION2
def josephus_survivor(people,steps) :
  liste = [i for i in range(1,people+1)]
  indeks = 0
  while len(liste) > 1 :
    indeks = (steps - 1 + indeks) % len(liste)
    liste.pop(indeks)
  return liste[0]

josephus_survivor(14,2)
 ... 13
