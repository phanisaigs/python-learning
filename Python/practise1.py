"""
range(1,100)
for i in range(1,100):
    print(i)

print(tuple(range(1,100)))


phanisai = input(" Enter the string that you want to check ")
i=0
for x in phanisai:
    print("The character present in",i, "value is", x)
    i+=1



for i in range(100):
    print(102.5 + 10.5 + 100.10 - 20)

# print the even and odd number using range and condition.

for i in range(21):
    if i % 2 == 0: #  this is equal 
        print(i)

for i in range (2,22,2):
    print(i)

for x in range(20,1, -2):
    print(x)
"""

list = eval(input("Enter some list data type number to validate."))
sum = 0
for x in list:
    sum = sum + x
print (" th total sum in the list is", sum)

