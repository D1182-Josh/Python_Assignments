    #TASK

# Kullanıcıdan alınan string'in içinde yine kullanıcıdan alınan substring kaç tane var onu sayma programı ?*



    #SOLUTION

text = input("")
sub_text= input("")
count = 0
for i in range(len(text)) :
  if text[i:i+len(sub_text)] == sub_text :
    count += 1
print(count)
