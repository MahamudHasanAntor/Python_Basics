# vowel and constraint check
char = input("Enter the alphabet : ")

if char == 'A' or char == "E" or char == "I" or char == "O" or char == "U":
    print (f"This alphabet-{char} is a vowel")

elif char == 'a' or char == "e" or char == "i" or char == "o" or char == "u":
    print (f"This alphabet-{char} is a vowel")

else :
    print (f"This alphabet-{char} is a constraint")

# Male Female , gender check
gender = input("Input Your Gender in one char : ")

if gender == "M" or gender == "m" :
    print ("Welcome sir in our Hotel")

elif gender == "F" or gender == "f" :
    print ("Welcome Mam in our Hotel")

else :
    print ("Sorry!!")

# even odd check
checknumber = int (input ("Enter the number : "))

if checknumber % 2 == 0 :
    print (f"This number -{checknumber} is even number")

else :
    print(f"This number-{checknumber} is odd number")

# leap year check
year = int(input("Enter the year : "))

if year % 4 == 0 and year % 100 != 0 :
    print ("This year is leap year")

elif year % 100 == 0 and year %  400 == 0 :
    print ("This year is leap year")

else :
    print ("This year is not leap year")

# vowel constraint check
check = input ("Enter the alphabet : ")

if check in "aeiouAEIOU" :
    print ("This alphabet is vowel")

else:
    print ("This alphabet is constraint")
    