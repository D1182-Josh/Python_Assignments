    #TASK

# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog " is a program, because it uses the letters A-Z at least once (case is irrelevant). Given a string, detect whether or not is a pangram. Return True if it is, False if not. Ignore numbers and punctuation. 

    #SOLUTION

cumle = input("").lower()
yeni_cumle = ""
alpha = "abcdefghijklmnopqrstuvwxyz"
for i in cumle :
  if i.isalpha() :
    yeni_cumle += i
print(set(alpha) - set(yeni_cumle) == set())    
