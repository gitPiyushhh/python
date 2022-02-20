class Student:
    school = 'PSIT'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def get_avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    def set_marks(self, m):
        self.m1 = m
    

p = Student(1,2,3)

print(p.get_avg())

