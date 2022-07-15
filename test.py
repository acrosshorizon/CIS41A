states = {}

file = open("USPresidents.txt", "r")

for line in file:
    line = line.split()
    if line[0] not in states:
        states[line[0]] = 1
    else:
        states[line[0]] += 1

print(states)
for key, value in states.items():
    print(f"{key} : {value}")