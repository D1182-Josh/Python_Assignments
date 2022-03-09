    #TASK

#   Given two arrays of string a1 and a2 return a sorted array r in lexicographical order of strings of a1 which are substrings of strings of a2.

    Example 1 :
        a1 = ["arp", "live", "strong"]
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        returns["arp", "live", "strong"]

    Example 2:
        a1 = ["tarp", "mice", "bull"]
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        return[]

    Notes:
#        Arrays are written in "general" notation. See "Your Test Cases" for examples in your language. In Shell bash a1 and a2 are string. The return is a string where words are seperated by commas. Baware: r must be without duplicates. 

    #SOLUTION1

a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

list(set([i for i in a1 for j in a2 if i in j]))

    #SOLUTION2

a1 = ["tarp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

list(set([i for i in a1 for j in a2 if i in j]))    

    


