'''
servers = ["ny-rt-101", "ny-rt-102", "ny-rt-800", "ny-rt-103","ny-rt-104"]
servers.append ("ny-rt-105")
print(servers)
servers.remove("ny-rt-102")
print(servers)
print("ny-rt-106" in servers)
servers.insert(0, "ny-rt-100")
servers.insert(5, "ny-rt-107")
print(servers)
servers.sort()
print("sorted server", servers )
servers.reverse()
print("Reverse order", servers)
print(id(servers))

services = ["nginx", "sshd", "docker", "mysql", "kubectl"]
print(services)
services.append("mysql")
services.append("mysql")
print(services)
services.remove("mysql")
print(services)
print(services[0])
print(services[2])
'''
# here the list of practises that list data type insertion order will be preserve, dupicates are allowed, data once added we can add some more data later also, slicing will be allowed.
# list is mutable that means we can add the data, remove the data, sort the data.Hetrogenous object allow means we can use of STR, BOOL, Float combing them to use in list data type.

x = [10,20,30,40,50]
x.append(60)
x.remove(50)
print(x)
b=bytes(x)
print(b)

# bytes data type: byte data type allow range 0 to 256 and its by nature is immutable that means once we assign the value it cannot be replaced.
# bytesarray data type: Bytes array data also same as bytes one changes is mutable using case for bytes and bytesarray when you want to extract binary content.
#Reading binary files (images, logs)

#Network communication
#Cryptography
#IoT/hardware programming
#Serialization and compression

'''
list data type :List data type can be used for group of objects,this is mutable 
1. insertion order should be preserved, dupicates are allowed, hetrogenous object is allowed growable based on our requirement like Also we should be using [] square bracket that will python using for list data type.
'''
servers = ["syd-rt-101", "syd-rt-102","syd-rt-103", "syd-rt-104" ]
print(servers)
servers.append("syd-rt-105")
servers.append("syd-rt-106")
servers.append("syd-rt-107")
servers.append("syd-rt-108")
servers.remove("syd-rt-102")
print(servers)
print ("First server using index", servers[0])
print("Second server using index is" ,servers[1])
print(" The third server using negative index", servers[-1])

# slicing operator to use to access the elements.
print ("The first server that will be using to get the slicing operator", servers[0:3])
print ("The first server that will be using to get the slicing operator", servers[3:6])

# the above mention once can be an example for access the element using positive index and negative index also slcing operator.

s = [10, "phanisai", True]
s1 = s*2
print (s)
 
# Tuple : Diffrence between list and tuple ius list data type is mutable annd tuple data type is immutable.
# tuple can be represent using () parenthesis.

servers_list = ("lon-rt-101", "lon-rt-102", "lon-rt-103" ,"50.8" ,True)
print(servers_list)

'''
the same logic will be applicable for tuple as well like list only once its updated canont be modified.
'''  

# Range data type: Range data type to represent the sequnce of values and its immutable.
# diffreent type of form is avaialble when we use range data type 
'''
Form 1 : range(10), it represent the values 0 to 9
Form2 : range (10, 99)
example of forms
Form1 : range (10) stop
form2: range (start and stop)
form3: range (start , step , stop)
 0 to end -1 

phanisai = range(100)
for i in phanisai: print(i)

meena = range(110,200)
print(meena[10])
print(meena[15])
print(meena[20])
print(tuple(meena[10:20]))
'''

harsha = range(10,100,20)
for i in harsha:print(i)


# Set data type: Insertion order will not preserved and duplicates are not allowded then we should use for sert data type {} curly brases will be used to represent the set data type.
phanisai = {10,20,30,10,20,30,}
print(phanisai)

# using the set data we can allow to add the duplicate collection but it will not print output.
#phanisai = {10,20,30,10,20,30,}
#print (phanisai[0])
# accessing the elements using indexing or slicing operator does now allow in set data type.
# insertion oder will not preserved.
# duplicates are not allowed.
# set data type is mutable that once we updated then we can add or remove the object from the collection.

s=set()
for i in range(100):
    s.add(i)
    print(s)

# Forzen set.
'''
all the features are same like set data type only changes is the frozenset is immutable that mean we cant add or remove the element once we set.
'''

# dictionary:
'''
dict can be represent in key : value pair.
key should be having unique value but value can be replaced.
ex: dictionary or phone book.
dict can be represent using {}
key can be any type also value can be any type we can use in dict
order will not preserved.
'''
phanisai = {100: "meena", 101: "harsha", 103:"sridevi"}
print(phanisai)

phani = {"phanisai":102, 20.32:"harsha.gp", 102:"canwe do this"}
print(phani)

d1={}
print(d1)
d1[100]="phanisai"
print(d1)
d1[101]=203.323232
print(d1)
d1[101]="harshagp"
print(d1)

# None data type.
def f1():
    a1 =10
    print(a1)
f1()
