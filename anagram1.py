    #TASK

#What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example: 'abba'&'baab'== true 
             'abba'%'abbba'==false
             'abba'&'abca'==false 
# Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:
        
        anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb','bbaa']
        anagrams('racer', ['crazer','carer','racar','caers','racer']) => ['carer','racer']
        anagrams('laser', ['lazing','lazy','lacer']] => []

        Note for Go
        For Go: Empty string slice is expected when there are no anagrams found

        #SOLUTION

def anagrams(word, word_list):
  return [i for i in word_list if sorted(list(word)) == sorted(list(i))]

anagrams("abba", ['aabb', 'abcd', 'bbaa', 'dada'])
... ['aabb', 'bbaa']


