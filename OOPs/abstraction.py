from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def process(self):
        print('Running..')

    
class B(A):
    def process(self):
        print('Running sub')

# a = A()  ## Now we can't make the instance of 'A'
b = B()
b.process()