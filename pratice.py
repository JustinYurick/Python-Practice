name = 'justin'
is_locked = True
num_list = [115,86,44,31]
iterating_num = 1


print('Hello my name is', name)
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

def sumNum(num1 , num2):
    print(num1 * num2)

def sumNumReturn(num1, num2):
    return num1 * num2

print('Two numbers sumed using print')
sumNum(2,4)

print('Two nums sumed using return', sumNumReturn(2,4))
