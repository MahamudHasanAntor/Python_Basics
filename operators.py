input1 = int(input("Enter your first number : "))
input2 = int(input("Enter your second number : "))
sum = input1 + input2
sub = input1 - input2
multipication = input1 * input2
print(f"sum : {sum}, sub : {sub}, multipication : {multipication}")
# in divison answer will be always float
number1 = 35
number2 = 7
print(f"Answer : {number1/number2}")
# but if we use floor division then the answer will be in floor division also we can use typecasting
print(f"in floor division answer will be : {number1//number2}")
number3 = 49
number4 = 8
number = number3/number4
number = int(number)
print(f"After typecasting the answer will be {number}")
# power of numbers
print(f"35 to the power 7  is {number1**number2}")
# to find reminders in division we are using mod
test1 = 37
test2 = 7
test = test1 % test2
print(f"after dividion betwwen {test1} with {test2} reminder is {test} ")
# conditional operators // here answer output will be in boolean (True and False)
print(10<12)
print(12<10)
print(12<=14)
print(12!=12)
print(12!=15)
print(12==12)
print(12==14)

# logical oparetors (and, or, not)
print (10<12 and 34>20 and 21>3)
print(10!=10 and 10<12 and 34>20)
print(10<12 or 10>19 or 10==19)
print(10==19 or 10==12 or 12<20)
print(not 10==12 and not 19==18 and 18>12 )
print (not 10==12 and not 19==18 and 18>19 )
print(12>10 and 10<29 or 29>90)
