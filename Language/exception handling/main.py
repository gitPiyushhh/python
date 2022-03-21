## Assume we are getting these values from user

a = 5
b = 0 ## Here if user inputs 0 then application crashes

#################################################
#### 1. Try block {for vulnerable statements}
try:
    print('Resource open..') # This resource should be closed even though exception is raised
    print(a / b)

#################################################
#### 2. Except block {for custom exceptions}
except Exception as e:
    print("Can't divide by zero😕")

#################################################
#### 2. Finally block {for expressions that need to be done at any cost}
finally:
    print('Resource closed..') 
