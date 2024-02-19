# separate each digit of a number and print it  on the new line
number = int ( input ("Enter your number : "))

while number > 0 :
    print ( number % 10, end =" " )
    number = number //10
    
# Pallindromic number 
initial = int ( input ("Enter your number : "))
copy = initial
reverse = 0

while initial > 0 :
    z = initial % 10 # if initial = 123 then z=123%10=3,z=12%10=2,z=1%10=1
    reverse = reverse * 10 + z # if initial = 123 then reverse is reverse=o*10+3=3, reverse= 3*10+2=32,reverse=32*10+1=321   
    initial = initial // 10 #if initial 123 then initial = 123//10=12, initial=12//10=1,

print (f"Reverse number is-{reverse}")

if reverse == copy :
    print (f"This number-{copy} is a pallindromic number")

else :
    print (f"This number-{copy} is not a pallindromic number")




