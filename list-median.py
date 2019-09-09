numbers = [-4.3, -6.7, -0.8, 1.2, 2.1, 2.6, 1.1]
numbers.sort()
sum = 0
for i in range(0, len(numbers)):
  sum += numbers[i]

length = len(numbers)
if (length %2 == 0):
    median = (numbers[(length)/2] + numbers[(length)/2-1]) / 2
else:
    median = numbers[(length-1)//2]

print ("Median " + str(median))
