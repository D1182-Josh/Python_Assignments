    #TASK

#"Loves me, loves me not " is a traditional game in which a person plucks off all the pedals of a flower one by one , saying the phrase "Loves me" and "Loves me not" when determining whether the one that love, loves them back. Given a number of pedals, return a string which repeats the phrases "Loves me" and "Loves me not" for every alternating pedaş, and return the last phrase in all caps. Remember to put a momma and space between phrases.

#    INPUT : 3 ---> "Loves me, Loves me no, LOVES ME"
#    INPUT : 6 ---> "Loves me,Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"
#    ınput : 1 ---> "LOVES ME"

    #SOLUTION1

n = int(input(""))
papatya = ["Loves me", "Loves me not" ]
yeni_papatya = []
if n == 1 :
  print(papatya[0].upper())
else:
  for i in range(1,n + 1) :
    if i % 2 == 1 :
      yeni_papatya += [papatya[0]]
    elif i % 2 == 0 :
      yeni_papatya += [papatya[1]]
  yeni_papatya  = yeni_papatya[:-1] + [yeni_papatya[-1].upper()]
  print(", ".join(yeni_papatya))

  
