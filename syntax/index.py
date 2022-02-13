########################################
############## Variables


# x = 5
# y = 3

# name = 'Piyush'

# print(name[1:4])  #4th char is excluded
# print(len(name)) 



########################################
############## Lists

# nums = [1, 2, 3, 4, 5]
# values = [2, 'Piyush', 1.5]

# # Lists in lists
# comb = [nums, values]

# print(nums[0:4])
# print(values)
# print(comb)

# # Methods 

# # 1. Add an element
# nums.append(6)
# print(nums)

# # 2. Remove an element
# nums.remove(6)
# print(nums)

# nums.pop(-1) #Remove the last element
# print(nums)

########################################
############## Touples {Immutable lists}

# tup = (1, 2, 3, 4)
# print(tup)


# tup[1] = 0  # 🚫 Assignment not supported

########################################
############## Set {Uniqle values}

# s = {1, 2, 1, 3, 2, 4}  # 1️⃣ Only 1 value
# print(s)

########################################
############## Dictionary {Like object literal}

# data = {1: 'Piyush', 2: 'Jonas'}

# print(data)
# print(data[2])

# print(data.keys())  # To get all the keys
# print(data.values()) # To get all the values

# print(data.get(3, 'Not found'))  # Search the key if not found then print 'Not found'

# keys = ['Piyush', 'Jonas']
# values = ['python', 'JS']

# pair = dict(zip(keys, values))


# print(pair)

## For finding the address of a variable
# from xml.etree.ElementTree import PI


# a = 5
# b = 5
# print(id(a))  #If the values of the variable is same then they both will have the same addrrss
# print(id(b))

# from numpy import var


# print(type(a))

#######################################
############# Type conversion


# a = 5.5

# print(int(a))


#######################################
############# Number system conversion

# a = 25

# print(bin(a))
# print(oct(a))
# print(hex(a))

# print(0b0101)  # Convert to the the decimal from binary
# print(0o0101)  # Convert to the the decimal from octal
# print(0x0101)  # Convert to the the decimal from hexa-decimal


#######################################
############# Swap 2 numbers

a = 5
b = 6

b,a = a,b

print(a,b) 