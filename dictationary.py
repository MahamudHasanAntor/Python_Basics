# in dictationary, its like list but here we will be working with keys and values

dictationaryTest = {0:"Mahamud Hasan", 1:"Mehedi Hassan Shohan", 2:"Dil Mahmud Khan", 3:"Monayem Hasan"} #here 1,2,3,4 is key and values are Mahamud Hasan,-- are values
print(dictationaryTest[1]) #here keys are working like indexing

dictationaryTest[4] = "Shakil Ahamed"


for i in dictationaryTest:
    print (i)

for i in dictationaryTest.values():
    print (i)

for i in dictationaryTest:
    print(dictationaryTest[i])

for i in range (0, len(dictationaryTest)):
    print (dictationaryTest[i])

aDictationaryTest = {1:"Mahamud Hasan", 2:"Mehedi Hassan"}
bDictationaryTest = {2:"Shakil Ahamed", 3:"Sanim Ahamed"}

aDictationaryTest.update(bDictationaryTest)

for i in aDictationaryTest.values():
    print(i, aDictationaryTest)

#Ref Link : https://www.geeksforgeeks.org/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/