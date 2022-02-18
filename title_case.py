#   TASK

#Astring is considered to be in title case if each word in string is either(a) capitalised(that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised. Write a function that will convert a string into title case, given an optinal list of exceptions (minor words). The list of minor words will be given as a string with each word seperated by a space. Yor function should ignore the case of the minor words string--it should behave in the same way even if the case of the minor word string is changed. First argument (required): the orginal string to be converted. Second argument(optinal): space-delimited list of minor words that must always be lowercase except for the first word in the string. 

 #   Example

    title_case('a clash of KING')
    minor_words('a an the of')
    Output: 'A Clash of King'


    title_case('THE WIND IN THE WILLOWS'),
    minor_words('The In')
    Output: 'The Wind in the Willows'


    #SOLUTION

#Output: 'The Wind in the Willows'
text = "THE WIND IN THE WILLOWS".lower().split()
minor = "The In".lower().split()
new_text = []

for i in text : 
  if i not in minor :
    new_text += [i.capitalize()]
  else :
    new_text += [i.lower()]

word = " ".join(new_text)
word = word[0].upper() + word[1:]
word    


