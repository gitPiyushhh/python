#########################################
######## pthon math library

import math

# 1. sqrt & pow()

x = math.sqrt(25)
print(x)

x = math.pow(5, 2)
print(x)

# 2. Floor & ceil()

x = math.floor(2.9)
print(x) ## No matter of the digit next to point will be the floor

x = math.ceil(2.1)
print(x)

########################################
########### Alias concept{Change name}

import math as m

print(m.pow(5, 2))