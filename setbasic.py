# in set item need to be unique that means we can use same value twice but it will be printed for one time
# also it is unordered that means in set indexing don't work, unchangable

setInformation = {"Mahamud Hasan", "Student", 23, "Student"}
print (setInformation) # setInformation will be print but problem is item-student will be print for one time 

setNumbers = [1,2,1,1,1,2,3,4,55,5,5,4,3]
setNumbers = set(setNumbers)
print (setNumbers)

for i in setInformation:
    print(i)

# for i in range (0, len(setInformation)):
#     print (setInformation[i]) # here we will get error beacause in set indexig dont work