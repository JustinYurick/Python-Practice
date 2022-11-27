import random
name = 'justin'
is_locked = True
num_list = [115, 86, 44, 31]
iterating_num = 1


# simple print statement
print('Hello my name is', name)

# to revrse a string we can use [::-1]
print('\nMy name backwards is', name[::-1])

if is_locked:
    print("\nIt is locked")
else:
    print('\nIt is unlocked')

for num in num_list:
    print(num)

while iterating_num <= 10:
    print(iterating_num)
    iterating_num = iterating_num + 1

# a funtion that doesnt return anything


def sumNum(num1, num2):
    print(num1 * num2)

# a function that does return something


def sumNumReturn(num1, num2):
    return num1 * num2

# default values can be given in funtions


def sumWithDefaults(num1=1, num2=1):
    return num1 * num2


print('\nTwo numbers multipled using print')
sumNum(2, 4)

print('\nTwo nums multipled using return', sumNumReturn(2, 4))

print('\nTwo nums multipled using default parameters ', sumWithDefaults())

# creating basic dictonary
contact_Info = {'Matt': '400-223-4124',
                'Greg': '213-234-1678',
                'Rachel': '558-465-5462'}

# how to access values
print('\n', contact_Info['Matt'])

# deleting key-value pairs
del (contact_Info['Matt'])
for contact in contact_Info:
    print('\n', contact)

# adding key-value pairs and also printing both values in a for loop
contact_Info['Matthew'] = '400-223-4124'
for name, phoneNum in contact_Info.items():
    print('\n', name, ':', phoneNum)

# dictonary with a list
numbers = {'Odd': [1, 3, 5, 7, 9],
           'Even': [2, 4, 6, 8, 10],
           'Prime': [2, 3, 5, 7]}
print('\n The first prime number is', numbers['Prime'][0])

# casting string to int
print('\nA string casted into and int', int('100'))
print('\nA int casted into and string', str(100))
print('\nA float casted into and int', int(2.3))

# requires "random" import
print('\nRandom Number from 1-100', random.randint(1, 100))
