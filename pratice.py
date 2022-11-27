name = 'justin'
is_locked = True
num_list = [115,86,44,31]
iterating_num = 1


#simple print statement
print('Hello my name is', name)

#to revrse a string we can use [::-1]
print('My name backwards is', name[::-1])

if is_locked:
    print("It is locked")
else:
    print('It is unlocked')

for num in num_list:
    print(num)

while iterating_num<= 10:
    print(iterating_num)
    iterating_num = iterating_num + 1

#a funtion that doesnt return anything
def sumNum(num1 , num2):
    print(num1 * num2)

#a function that does return something
def sumNumReturn(num1, num2):
    return num1 * num2

print('Two numbers sumed using print')
sumNum(2,4)

print('Two nums sumed using return', sumNumReturn(2,4))
