lower = 900
upper = 1000

print("Prime numbers between",lower,"and",upper,"are:")

for num1 in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num1 > 1:
       for i in range(2,num1):
           if (num1 % i) == 0:
               break
       else:
           print(num1)
