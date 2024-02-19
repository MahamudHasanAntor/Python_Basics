#convert a datatype to different daatatype -- Type Casting
a = "12"
print(type(a))

a = int(a)
print(a)

b = int(a) # we can assign the values in different varibals
print(b, type(b))

flo = 34.60
newint = int(flo)
print(newint)

flo = float(newint) 
print(flo)

#boolean

test1 = 0
test2 = 0.0
test3 = "" #[]
test4 = None
test5 = 0.5

test6 = 1.1
test7= 900.923
test8= 100
test9 = "Mahamud"

checktest1 = bool(test1)
checktest2 = bool(test2)
checktest3 = bool(test3)
checktest4 = bool(test4)
checktest5 = bool(test5)
checktest6 = bool(test6)
checktest7 = bool(test7)
checktest8 = bool(test8)
checktest9 = bool(test9)

print(checktest1, checktest2, checktest3, checktest4, checktest5, checktest6, checktest7, checktest8, checktest9)

# string to integer

numbers = "1234"
changenumbers = int(numbers)
print(changenumbers, type(changenumbers))