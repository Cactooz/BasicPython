numbers = [-4.3, -6.7, -0.8, 1.2, 2.1, 2.6, 1.1]
numbers.sort()
sum = 0
for i in range(0, len(numbers)):
  sum += numbers[i]

average = sum / len(numbers)
print ("Average " + str(average))
averageRound = round(average, 2)
print ("Average rounded " + str(averageRound))
