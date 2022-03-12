    #TASK

#   Write  a Paython program to find the minimum window in a given string which will contain all the characters of another given string.

    #SOLUTION1

s1 = "Çanakkale"
s2 = "lan" #output "anak"
index_no = []
for i in range(len(s2)) :
  if s2[i] in s1 :
    index_no += [s1.index(s2[i])]

index_no.sort()
l = len(index_no) #3
h = int(index_no[l-1]) + 1 

for i in range(l,h) :
  print(s1[i], end= " ")

  #SOLUTION2

string = "çanakkale"
pattern = "çnk"
  
# let's find the index of r and g in String and the
# stor them in index list (index[]) 
index=[]
for x in range(len(pattern)):
    if pattern[x] in string:
        index.append(string.index(pattern[x]))
  
# sorting the r and g index's
index.sort()
  
# save first index in l
l = len(index)
low = int(index[0])
  
# save  last index in h
high = int(index[l-1])
h = high +1
for i in range(low,h):
    print(string[i],end=" ")



