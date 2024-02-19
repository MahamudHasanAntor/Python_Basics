# string indexing

name ="Mahamud"

print (name[0]) #postive indexing
print (name[1])
print (name[2])
print (name[3])
print (name[4])
print (name[5])
print (name[6])

print (name[-1]) #negetive indexing
print (name[-2])
print (name[-3])
print (name[-4])
print (name[-5])
print (name[-6])
print (name[-7])

# string slicing
name = "Mahamud Hasan"
print (f"Hi {name[8:13:1]}") #here we use range function for slicing string ,, we can keep like [8:] this , then print rest of index automatic way
save = name[0:7] # we can save in variable
print(f"Hello {save}")

# to find length of string we are using len() function
name = "Mahamud Hasan"
print (f"Length of 'Mahamud Hasan' is -{len(name)} ")

# two ways iterating over strings // loop in string
message = "Hello, How are you"
if "Hello" in message :
    print (True)

for i in message :
    print(i)

for i in range(0, len(message), 1):
    print(message[i], end="")

# we can find string method like upper(), count() in w3 schools website