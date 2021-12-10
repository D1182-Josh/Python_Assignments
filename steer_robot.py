#steering a robot in python#

command = ["right 20", "right 30", "left 50", "up 10", "down 20"]

for i in range(len(command)) :
    if command[i].startswith("r") : x = x + int(command[i].split()[1])
    elif command[i].startswith("l") : x = x - int(command[i].split()[1])
    elif command[i].startswith("u") : y = y + int(command[i].split()[1])
    elif command[i].startswith("d") : y = y - int(command[i].split()[1])

[x, y]
