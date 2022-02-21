###############################################
####### DUCK TYPING


# class Pycharm:

#     def execute(self):
#         print('Compiling')
#         print('Executing')

# class VsCode:

#     def execute(self):
#         print('Spell Check')
#         print('Convention check')
#         print('Compiling')
#         print('Executing')
    

# class Laptop:

#     def code(self,ide):
#         ide.execute()

# ## We can use pycharm
# # myIDE = Pycharm()


# ## We can use VS Code as well
# myIDE = VsCode()

# lap1 = Laptop()

# lap1.code(myIDE)


###############################################
####### OPERATOR OVERLOADING

a = 5
b = 6

## Everything with the help of Objects

## This is the inbuilt python method to 'add'
print(int.__add__(a,b))


## We can not add 2 objects through it{So we should overload it🙂}
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3
    
    def __gt__(self,other):
        total1 = self.m1 + self.m2
        total2 = other.m1 + other.m2
        if total1 > total2:
            return True
        else: 
            return False

s1 = Student(1,2)
s2 = Student(3,4)


s3 = s1 + s2
print(s3.m1)

winner = None


if s1 > s2:
    print("winner is s1")

else: 
    print("winner is S2")

###############################################
####### METHOD OVERRIDING

class Test:
    
    def show(self):
        print("In 'A' Show")
    

class TestChild(Test):
    ## Override {show fct of parent class}

    def show(self):
        print("In 'B' Show")
    

a = TestChild()
a.show()