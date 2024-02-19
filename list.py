list1 = ["Mahamud", "Hasan", 23, "Male", "Student"]
print(type (list1))

list1[0] = "Mahamud Hasan" #list is mutable while string is not
list1[1] = "Student"
print(type(list1[2]))

print (list1[0]) #positive indexing
print (list1[1])
print (list1[2])
print (list1[3])
print (list1[4])

print (list1[-1]) #negetive indexing
print (list1[-2])
print (list1[-3])
print (list1[-4])
print (list1[-5])

print (list1[1:]) #string slicing

for i in list1:
    print(i)


for i in range (0, len(list1), 1):
    print(list1[i])

# append insert pop

number = [1, 2, 3, 4]
number.append(100) # by using append list will be , number = [1,2,3,4,100]
print (number)
#there are lots of list method, need to check it out from w3schools website

#insert a value in a list
insertTest =[1,2,3,4,5]
insertTest.insert(2, 100) #insertTest = [1,2,100, 3,4,5]
print (insertTest)

# by using pop , we can remove value from list

popTest = [1,2,3,4,5]
popTest.pop()
print(popTest)
popTest.pop(1)
x = popTest.pop(1)
print(popTest)
print(x)

# also we can remove item from list by using remove list method

removeTest = [20,30,30,30,20,20,20,2,1,2]
removeTest.remove(20)
print(removeTest)



# note, important

aNumber = [1, 2, 3, 4, 5]
bNumber = aNumber #here bNumber is not saving the values of aNumber, it is just create a access point for aNumber
print (bNumber) # bNumber is just accessing the aNumber 
bNumber[0] = 20 # here aNumber[0] will be change
print (aNumber)