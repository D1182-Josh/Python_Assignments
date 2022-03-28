    #TASK

# Given a list of integers and a single sum value, return the first two values
(parse from the left please) in order of appearance that add up to form the sum.
sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
== [3, 7]
#Negative numbers and duplicate numbers can and will appear.
#NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements.
#Be sure your code doesn't time out.

        #SOLUTION

        
