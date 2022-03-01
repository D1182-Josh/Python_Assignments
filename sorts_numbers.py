    #TASK

#Write a function that sorts the positive numbers in ascending order, and keeps the negative numbers untouched. 
    Examples 
    pos_neg_sort([6, 3, -2, 5, -8, 2, -2]) --> [2, 3, -2, 5, -8, 6, -2]
    pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]) --> [1, 2, 3, -1, 4, 5, -1, 6]
    pos_neg_sort([-5, -5, -5, -5, 7, -5]) --> [-5, -5, -5, -5, 7, -5]
    pos_neg_sort([]) --> []


    #SOLUTION1

arry = [6, 3, -2, 5, -8, 2, -2]
sıra_no = ""
pozitif = []
negatif = []

for i in arry :
  if i > 0 :
    pozitif.append(i)
    sıra_no += str(arry.index(i))
  else:
    negatif.append(i)

pozitif.sort()
no = 0
for i in sıra_no :
  negatif.insert(int(i), pozitif[no])
  print(negatif)
  no += 1

print(negatif)

    #SOLUTION2

arry = [6, 3, -2, 5, -8, 2, -2]
positive = []
negative = []
indeks = ""

for i in arry :
  if i > 0 :
    indeks += str(arry.index(i))
    positive += [i]
  else:
    negative += [i]
count = 0
for i in indeks :
  negative.insert(int(i), sorted(positive)[count])
  count += 1

print(negative) 


