number = int ( input ("Enter your number : "))

for i in range (1, number+1, 1) :
    print (number)

number = int ( input ("Enter your number : "))

for i in range (number, 0, -1):
    print (number)

# number table
table = int ( input ("Which table you want : "))

limit = int ( input ("How many times you want to multiply : "))


for i in range (1, limit+1):
    print (f"{table} * {i} = {table*i}" )

# sum upto n termas
number = int ( input ("Enter your number : "))
a = 0
for i in range (1, number+1, 1):
    a = a+i
    
print(a)

# factorial
number = int ( input("Enter you number for factorial : "))
fact = 1
for i in range (1, number+1, 1):
    fact = fact * i

print (fact)
    

# print all the facors of a numbers
number = int (input("Enter the number for print all the factors : "))

for i in range (i, number + 1, 1):
    if number % i == 0:
        print (i)
        # print (i, end= " ") for print all the factors in one line

# check if it is a perfect numbers
number = int ( input("Enter the number to check perfect number : "))
fact = 0

for i in range (1, number, 1):
    if number % i == 0 :
        fact = fact + i

if fact == number :
    print ("This is a perfect number ")

else :
    print ("Sorry this is not a perfect number")