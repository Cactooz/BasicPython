start = 1000
finish = 1500
i = 0

while (start<=finish):
  start = start * 1.02
  i = i + 1
  print start

print ("Reached " + str(finish) + " after " + str(i) + " times")
