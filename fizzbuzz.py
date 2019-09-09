print ("FizzBuzz")
num = input("Write any number: ")
if (num %3 == 0 and num %5 == 0):
  print ("Fizzbuzz")
elif (num %5 == 0):
  print ("Buzz")
elif (num %3 == 0):
  print ("Fizz")
else:
  print num
