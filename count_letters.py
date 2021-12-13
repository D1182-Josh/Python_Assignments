Task:

Count the number of each letter in a sentence.
The department you work for undertook a project construction that makes word / text analysis. You are asked to calculate the number of letters or any chars in the sentences entered under this project.
Write a Python program that;
takes a sentence from the user,
counts the number of each letter of the sentence,
 collects the letters/chars as a key and the counted numbers as a value in a dictionary.


hippo runs to us!	
{'s': 2, 'r': 1, 't': 1, 'h': 1, 'n': 1, 
'i': 1, 'u': 2, 'o': 2, 'p': 2, ' ': 3, '!': 1}  #

1.solution:

sent = input("Write a sentences: ")
dictionary = dict()
for i in sent:
    dictionary[i] = sent.count(i)
    
print(dictionary)

2.solution:

 sentence = input("Enter a sentence: ")
word = {}
for i in sentence :
  if i in word:
    word[i] += 1
  else:
    word[i] = 1
print(word)       

