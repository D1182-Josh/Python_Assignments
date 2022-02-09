    #TASK

# You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' score. At the beginning of the game, you start with an empty record. You are given a list of string ops, where ops[i] is the iᵗʰoperation you must apply to the record and is one of the following:
    1. An integer x -Record a new score of x,
    2. "+" -Record a new score that is the sum of the previous two scores . It is guaranteed there will always be two previous scores.
    3. "D"  -Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
    4. "C" -Invalidate the previous score, removing ,t from the record. It is guaranteed there will always be a previous score.

    Return the sum of all scores on the record.

    Input: ops=["5", "2", "C", "D", "+"]
    Output: 30 
    Explanation:
        "5" - Add 5 to the record, record is now [5]
        "2" -Add 2 to the record, record is now [5, 2].
        "C" - Invalidate and remove the previous score, record is now [5]
        "D" -Add 2 * 5 = 10 to the record, record is now [5, 10]
        "+" -Add 5 + 10 = 15 to the record, record is now [5, 10, 15]
        The total sum is 5 + 10 + 15 = 30

     #SOLUTION

ops = ["5","-2","4","C","D","9","+","+"]
total = []
for i in range(len(ops)):
  if ops[i]=='C':
    total.pop()
  elif ops[i]=='D':
    total.append(2*total[-1])
  elif ops[i]=='+':
    total.append(total[-1]+total[-2])
  else:
    total.append(int(ops[i]))
print(sum(total))     
