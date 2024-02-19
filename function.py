# function basically do specefic task
# when we are defining function that time we use parameter and when we are calling function that time we use arguments
def hello () :
    print("Hello world")

hello()

def parameterArgument(a,b,c): #here a,b,c are parameters , and these are normal parameter
    print(a+b+c)

fnumber = int(input ("Enter your first number: "))
snumber = int(input ("Enter your second number: "))
tnumber = int(input ("Enter your third number:"))
parameterArgument(10,12,15) #here 10, 12, 15 are arguments that means a=10, b=12, c=15
parameterArgument(fnumber, snumber, tnumber)

# default parameter
def deParameter(a,b,c,d=10): #here we assign value of d, thats the example of default parameter
    print(a+b+c+d)

deParameter(19,23,22) #because here we didn't assign value of d

# default arguments
def deArguments(a,b):
    print(a+b)

deArguments(10,20)#here we assign value of a and b, thats why it is example of default arguments

#keyword arguments
def keyArguments(a,b,c,d):
    print(a+b+c+d)

keyArguments(b=20, c=20, a=10, d=21) #here it is example of keyword arguments, here keyword is a,b,c,d

#even odd by using function
def evenORodd (number):
    if number%2==0 :
        print(f"This number-{number} is a even number")

    else :
        print(f"This number-{number} is a odd number")

number = int (input ("Enter your number to check even or odd : "))
evenORodd(number)

# return despite of using print
# return -- return value from the function where we call the function

def returnTest (number) :
    if number % 2 == 0 :
        return ("even") #if even then it will return to where we call the function 
    else :
        return ("odd") #if odd then it will return to where we call the function
    
# returnTest(14)
# print (returnTest(14))
result = returnTest(14) # we can save in a variable
print (result)