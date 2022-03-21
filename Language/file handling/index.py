###################################
##### 1. File importing

f = open('data', 'r')


## Methods on the imported file
print(f.read())
# print(f.readline())

######################################
#### 2. Writing on the File

f = open('data-write', 'w') ## @overwrite all previos data
f.write('Hello world!')

f = open('data-write', 'a') ## append to previos data
f.write(' ## This is appended data...')

f = open('./pic.jpg', 'rb') ##'rb' --> 'read binary'
fc = open('pic-copy.jpg', 'wb') ##'wb' --> 'write binary'

for i in f:
    fc.write(i) 