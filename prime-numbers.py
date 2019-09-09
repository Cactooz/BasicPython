num = int(input("Write any number: "))
if (num > 1):
#Going through all numbers from 2 to the chosen number
   for i in range (2, num):
      #If the number divided by i is equal to 0 then it's not a prime number.
       if (num %i == 0):
           print (str(num) + " is not a prime number")
           break
   else:
       print (str(num) + " is a prime number")
#If the number is less than or equal to 1 then it is not prime number.
else:
   print (str(num) + " is not a prime number")
