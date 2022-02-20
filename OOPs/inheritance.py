class Parent:
    def __init__(self):
        print('A init')

    def f1(self):
        print("Feature 1 called")

    def f2(self):
        print("Feature 2 called")

'''
## 1. Single lvl inheritance
class Child(Parent):  
    ## This class is inheriting the parent class
    def f3(self):
        print("Feature 3 called")
    

## 2. Multi lvl inheritance {Grand Child --> Child --> Parent😌}
class GrandChild(Child):
    pass
'''

## 3. Multiple inheritance {GrandChild --> Child && GrandChild --> Parent🙂}

class Child():
    def __init__(self):
        print('B init')

    def f3(self):
        print("Feature 3 called")


# class GrandChild(Child, Parent):  
#     pass


# g1 = GrandChild()

#######################################################
########### SUPER KEYWORD {Call method of parent}

class GrandChild(Parent):
    def __init__(self):
        super().__init__()
    
    def called(self):
        super().f1()
        

g1 = GrandChild()
g1.called()