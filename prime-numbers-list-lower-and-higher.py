lowerNumber = int(input("Write the number to check from: "))
topNumber = int(input("Write the number to check to: "))
for num in range(lowerNumber, topNumber + 1):
   #If the number is less than or equal to 1 then it is not prime number.
   if (num > 1 and topNumber >= lowerNumber):
       for i in range(2, num):
         #If the number divided by i is equal to 0 then it's not a prime number.
           if (num %i == 0):
               break
       else:
           print (num)
