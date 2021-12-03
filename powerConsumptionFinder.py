testArray=[0, 0, 1, 1]

columnCount = 0
f = open(R"C:\Projects\advent-of-code\Day3\day3Data.txt", "r")

data = []


columnCount = len(data)


for line in f:
    data.append(line)


column = []
for i in range(columnCount):
    column[i] = []
print (columnCount)
print(data[0])
counter = 0
for row in data:
    for num in row:
        column[counter].append(num)
        counter +=1
        if counter == 12:
            counter = 0

