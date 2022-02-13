########################################
####### Taking input from user

from sys import argv


name = input("Enter your name: ") 
print(name)  

#########################################
####### Attaching values with the string{in output}

print('Hello {}✋🏻'.format(name))


x = int(input("First no: "))  # note: This will always take the input as a string so convert to int
y = int(input("Second no: ")) 

print(x + y)

#########################################
####### 'argv' for runtime value pass {argv --> argument values}

x = int(argv[1]) 
y = int(argv[2])

print(argv[0]) ## This is the file name
print(x + y)