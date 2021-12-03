
f = open(R"C:\Projects\advent-of-code\Day1\day1Data.txt", "r")

data = []
increases = 0
for line in f:
    data.append(int(line))

organizedData = []
def MeasurementWindow(list, windowSize):
    i = 0
    for key, value in enumerate(data[:-windowSize]):
        val0 = (value + data[key + 1] + data[key + 2])
        val1 = (data[key + 1] + data[key + 2] + data[key + 3])
        if val1 > val0:
            i += 1
    return i


def incOrDec(firstNum, secondNum):
    return firstNum < secondNum

def depthMeasurement(numArray):
    for i in range(len(numArray)-1): 
        if incOrDec(numArray[i], numArray[i+1]):
            global increases
            increases+=1
    return increases
print (depthMeasurement(data))
print(MeasurementWindow(data, 3))
