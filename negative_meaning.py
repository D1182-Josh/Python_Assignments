#Define a function to take a word and return negative meaning.
#Given a word, return a new word where "not " has been added to the front. 
# However, if the word already begins with "not", return the string unchanged.

#For example:   print(not_string('sugar'))   ---->    not sugar



def not_string(word):
    if "not" in word:
        return word
    else:
        return "not " + word