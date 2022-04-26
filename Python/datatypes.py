#I. Numeric Data Types
#1. Integer

n=int(input("Enter the integer value for n: "))
print("The value of n is: ",n," and the type of n is: ",type(n))

#2.Integer
n=float(input("Enter the float value for n: "))
print("The value of n is: ",n," and is of the type: ",type(n))

#Complex
n=complex(input("Enter the complex value of n: "))
print("The value of n is: ",n," and is of the type: ",type(n))


#II. Sequence Type (Ordered Collection of Data)
# [ You can also use string in double or triple quotes]

#1. String
n=input("Enter the string value: ")
print("The value of string value for n is: ",n," and the type of n is: ",type(n))

#1.1 Accessing String Elements: [by indexing] 
# [use +ve integers to access it from front, use -ve integers to access it from back]

print("The First element is: ",n[0])
print("The last element is: ",n[-1])

#2. List[by indexing] 
#  [use +ve integers to access it from front, use -ve integers to access it from back]
n=list(input("Enter the value for list n: ").split())
print("The value of list n is: ",n," and of the type: ",type(n))

# 2.1 Accessing the string elements
print("The first element of list n is: ",n[0])
print("Thge last element of list n is: ",n[-1])

# 3. Tuples (Similar to the list: but it is immutable)
n=tuple(input("Enter the value for tuple n: ").split())
print("The calue of Tuple n is: ",n," and is of the type: ",type(n))

#3.1 Accessing Tuple Elements
print("The first element of Tuple n is: ",n[0])
print("The last element of tuple n is: ",n[-1])

#3.2 Try to modify the tuple elements
# n[0]=2
# You will receive an error as tuples can't be modified (TypeError: 'tuple' object does not support item assignment)

# Tuple packing and unpacking yet to be covered


#III Boolean

n=input("Enter the Boolean Value")
if(n=='True'):
    n=True
elif (n=='False'):
    n=False

if(type(n)==bool):
    print("The value of boolean n is: ",n," and is of the type: ",type(n))


# IV Set [Unordered Collection of Data that is iterable, mutable and has no duplicate elements]

n=set(input("Enter the value of set n: ").split())
print("The value of set n is: ",n," and of the type: ",type(n))
# Observe that the order is not in sequence, so be careful while using this data type

# See if you can access the elements by Index
# print(n[0])
# TypeError: 'set' object is not subscriptable (which means it can't be accessed by indexing)
# for traversing, use the element itself

for item in n:
    print(item)

# V Dictionary (It is also unordered, values are stored like a map, holds key:value pair)
n={}
key=[1,2,3]
value=[4,5,6]
for i in range(0,3):
    n[key[i]]=value[i]

print(n)



# Practiced from GEEKSFORGEEKS (https://www.geeksforgeeks.org/python-data-types/)





