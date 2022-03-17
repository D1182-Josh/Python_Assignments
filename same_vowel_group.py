    #TASK

#Write a function that select all words that have all  the same vowel (in any order and /or number) as the first word, indluding the first word.
#Examples 
    same_vowel_group(["toe", "ocelot", "maniac"]) --> ["toe", "ocelot"]
    same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]) --> ["many"

#            Notes: Words will contain only lower case latter, and may contain whitespaces. Frequency does not matter ( e.g. if the first word is " loopy", then you can include words with any number of o's, so long as they only contain o's, and not other vowels).

    #SOLUTION1

words = ["hoops", "chuff", "bot", "bottom"]
new_words = []
for i in words :
  for j in i :
    if j not in "aeiou" :
      i = i.replace(j, "")
  new_words += [i]
same = [words[0]]
for i in range(1,len(new_words)) :
  if set(new_words[0]) == set(new_words[i]) :
    same += [words[i]]

print(same)
    ...['hoop', 'bot', 'bottom']

        #SOLUTION2
    
def same_vowel_group(words):
    new_words = []
    for i in words :
        for j in i :
            if j not in "aeiou" :
                i = i.replace(j, "")
        new_words += [i]
    same = [words[0]]
    for i in range(1,len(new_words)) :
        if set(new_words[0]) == set(new_words[i]) :
            same += [words[i]]
    return same
same_vowel_group(["hoops", "chuff", "bot", "bottom"])

    ...['hoop', 'bot', 'bottom']
