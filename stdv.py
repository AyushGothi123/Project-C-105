import statistics
import math

data = [60,61,65,63,98,99,90,95,91,96]

def mean(data):
    n = len(data)
    total = 0
    for i in data:
        total += int(i)
        

    mean = total/n
    return mean


squared_list = []
for number in data:
    a = int(number) - mean(data)
    a  = a**2
    squared_list.append(a)

sum = 0
for i in squared_list:
    sum += i

result = sum/(len(data)-1)
standardDeviation = math.sqrt(result)
print(standardDeviation)
