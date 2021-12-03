horizontal = 0
depth = 0
aim = 0

directions = []
magnitudes = []
x = []
f = open(R"C:\Projects\advent-of-code\Day2\day2Data.txt", "r")


def calculatePosition(vectorArray):
    direction =vectorArray[0] 
    magnitude =int(vectorArray[1])
    if(direction == "forward" ):
        global horizontal
        global aim
        global depth
        horizontal += magnitude
        depth += aim * magnitude

    elif(direction == "up" ):
        aim -= magnitude
    elif(direction == "down"):
        aim += magnitude

for line in f:
    x = line.split()
    calculatePosition(x);

print(depth * horizontal)
