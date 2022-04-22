    #TASK

            
#Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]

    #SOLUTION

def duz_liste(liste):
  if not isinstance(liste, list):
    return [liste]
  elif not liste:
    return []
  else:
    return duz_liste(liste[0]) + duz_liste(liste[1:])

arry = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(duz_liste(arry))

...  [1, 'a', 'cat', 2, 3, 'dog', 4, 5]

    
