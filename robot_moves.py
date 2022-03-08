    #TASK

#There is a robot starting at the position (0,0), the orijin, on a 2D plane. Given a squence of its movesi judge if this robot ends up at (0,0) after it completes its moves. You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U'(up), and 'D' (down). Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise. Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move. 
    Example 1:
        Input: moves = "UD"
        Output : true
    Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true. 

    #SOLUTION

moves = "LLLUUD"
x,y = 0 , 0
for i in moves :
  if i == "L" : x += 1
  elif i == "R" : x -= 1
  elif i == "D" : y -= 1
  elif i == "U" : y += 1 

print(True if x == 0 and y == 0 else False)     
