import random
import string


charValues= string.ascii_letters + string.digits + string.punctuation

length= int(input('Enter length of password: '))
password= "".join([random.choice(charValues) for i in range(length)])
#for i in range(length):
 #   password+=random.choice(charValues)

print('Generated password is:',password)    