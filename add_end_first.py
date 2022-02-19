#   TASK

#   Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched. 
    Examples:

pig_it('Pig latin is cool') # igPay atinlay siay coolcay
pi_it('Hello world !') # elloHay orldway !

    #SOLUTION1

text = "Hello world !".split()
new_text = []
for i in text :
  if i.isalpha() :
    new_text.append(i[1:] + i[0]+ "ay")
  else :
    new_text.append(i)

" ".join(new_text)

    #SOLUTION2

" ".join([i[1:] + i[0]+ "ay" if i.isalpha() else i for i in input("").split()])


