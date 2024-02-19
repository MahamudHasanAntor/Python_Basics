# in tuple, it is immutable in tuple we will be using ()

information = ("Mahamud Hasan", "Male", 23, "Student")

print (f"Name : {information[0]}")

tupleTest = [1, 2, 3, 4, 5]
tupleTest = tuple(tupleTest) # also we can  create tuple like this way
print (tupleTest)

for i in range (0, len(information)):
    print (information[i])

for i in information:
    print(i)

# tuple unpacking

tupleUnpacking = (1, 2, 3, 4, 5)
a,b,c,d,e = tupleUnpacking # here tuple will be unpacked, means a= 1, b=2, c=3, d=4, e=5
print (f"First number-{a}, Second Number-{b}, Third Number-{c}, Fourth Number-{d}, Fifth number-{e}")
