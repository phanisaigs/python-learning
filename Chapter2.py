#-----------------------------------------------------------------
# Immutable Vs Fundamenal data types
#-------------------------------------------------------------------

# whenver we create an object that has been assignes variable value  the value will remain the same for the object and if you assign the new value for that variable then the new object will creatre 
# to that variable that kind of nature is called Immutable.
# Mutable : The value can be changed
# Immnutable : the value cannot be changed.
# all the fundamental datatype of immnutable here the exampe for that to check.
x = "Welcome phanisai for improving the knowledge in python"
print ("ID the memory allocated:", id(x))
print(x)

x = "Welcome phanisai for improving the knowledge in python now the object that is stored in the memory is changed"
print ("ID the memory allocated:", id(x))
print(x)

x = 10
print (id(x))
y = 10
print (id(y))

# here the example of wheneve we use the same value of the object then the pythong will default same memory object for all the varialbe that rererecer to that value.
# why pythoon fundamental data types are immputable that mean the object will not the same with variable.
'''
Here the Voter system that we can use for that example 
V1 :"Bangalore"
V2 : "Bangalore"
V3 : "Bangalore"
V100 : "Bangalore"

now the python user V1, V2 V3 as same refrence object like Bangalore to all the people now if one person want to change the location then it will break for all the user now what python will do is
instead of that it will create new object like 
V100 : "Mysore"
the old members will reamin the same this new person object has been create and memory allocation has been changes here the example for that.
'''
v1 :"Bangalore"
V2 :"Bangalore"
V3 :"Bangalore"
V100 :"Bangalore"
print(id(v1))
print(id(v2))
print(id(v3))
print(id(v100))


'''
Advance data types that we are in progression like 
1. bytes
2. bytesdarray
3.list
4.tuple
these are the data types we can use to represent the group of data types 
'''