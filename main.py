stack = [("R", "N", "P", "G"),
         ("T", "J", "B", "L", "C", "S", "V", "H"),
         ("T", "D", "B", "M", "N", "L"),
         ("R", "V", "P", "S", "B"),
         ("G", "C", "Q", "S", "W", "M", "V", "H"),
         ("W", "Q", "S", "C", "D", "B", "J"),
         ("F", "Q", "L"),
         ("W", "M", "H", "T", "D", "L", "F", "V"),
         ("L", "P", "B", "V", "M", "J", "F")]

command = []
command_number = []
message = ""

with open("crane.txt", "r") as file:
    for line in file:
        command.append(line)

print(command)
print(len(command))

for item in command:
    # number
    number_1 = int(item.partition(" ")[2].partition(" ")[0])
    # from
    number_2 = int(item.partition(" ")[2].partition(" ")[2].partition(" ")[2].partition(" ")[0]) - 1
    # to
    number_3 = int(item.partition(" ")[2].partition(" ")[2].partition(" ")[2].partition(" ")[2].partition(" ")[2].partition("\n")[0]) - 1
    command_number.append((number_1, number_2, number_3))
print(command_number)

for command in command_number:
    for i in range(0, command[0]):
        temp = stack[command[1]][-1]
        stack[command[2]] = list(stack[command[2]])
        stack[command[2]].insert(len(stack[command[2]]), temp)
        stack[command[2]] = tuple(stack[command[2]])
        stack[command[1]] = stack[command[1]][:-1]

for i in range(0, len(stack)):
    message = message + (stack[i][-1])

print(message)
