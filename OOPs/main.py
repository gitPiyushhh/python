#######################################
######### Classes

class Computer:
    company = 'asus'

    ## Constructor
    def __init__(self, processor, ram):
        self.processor = processor
        self.ram = ram

    
    ## Methods
    
    def get_config(self):
        print("{}, {}, 512gb-SSd".format(self.processor, self.ram))

comp1 = Computer('i5', '8gb')
comp2 = Computer('i7', '16gb')

comp1.get_config()
comp2.get_config()
print(comp1.company)  
