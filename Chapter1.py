# disussion abourt variable in python.
'''
1 python is case sensitive that means A variable will not be the same smalle letter a
2 variable name should not start with number but it can be used in the middile.
3 Reserved words cannot be used in variable name.
4 _ when we use these underscore in the pythn variable name then its private.
'''

phanisai =10
Meena=30
print (phanisai+Meena)

# the above one simple example that has been used for varialbe along with operation concept.

'''
Data types in python
1. int : int datatype represent the value of integer 0 to 9
2. string : string data type we can represent the data in string that means words with double quotes or single quotes
3. float : float data types that we can represent using flaot value like 3.1,5.1,8.4 like 
4. Boolean : only two condition can apply to variable either the condition is TRUE or FALSE.
5. complex: to complex calculation.
6.bytes
7. bytesarray
8.range :
9. list 
10. tuple:
11. set data type
12. frozen set.
13.dict
14.None 
'''
'''
x =80 # integer
y = "welcome python again in my life for learning" # string 
z = 8.4 # float
a = True # boolean
print (x,y,z,a)
print (type(x), type(y), type(z), type(a) )
print (id(x), id(y))

# these are the example for data type that is avaialble in the built in function that are avaialble in python.
'''
a = 10
b = 20
result = a > b
print (result) 

'''
Here we have one more data the that we are using Boolean here we have two condirtion that True or False
Always the first letter should start with capital.

this is one of the usefull condition if the greater than or lesser than situation, condition statment, even number or odd number these situtaion we can use.

'''

# 21-06-2025
# STR data type : Any sequence of charater that are represent in double quotes or single quotes that is consider as STR data type in python.
# if you want to use the STR in single  line  character you can use '' or "" 
# if you want to use multi line strings the you have to ''' 

a = ''' this is phanisai testing the multline strings
      we are using to print that to valid using VS code'''
print (a)

#slice operaotor

a = "phanisai to test the slicing operator concept"
b= a[3:5]
print(b)

# Need to understand the concept called indexing 
# indexing alway start with 0 from left to right combination.
# the below code we can use to check the indexing as well slicing operator.
s="phani"
s[0]

varialbe = "testing to print the slicing the concept to print the woord"
phanisai = varialbe [0:18]
print(phanisai)

# these print function can use slicing operator to print the exact word.
# use case of this is when we use the variable to print it will print all the character but when we want to print the exact word we can use this cocenpt.
