# comments

# variable

# print('hello world')
# print('sainaveen')

# name ='Hare krishna'
# age = 25
# print(name)
# print(age)
# full_name = 'Harekrishna'
# print(full_name)

width, height = 400, 500
print(width)
print(height)

your_name = input('please enter your name: ')
print(your_name)
print('hi' + your_name)

num1 =  input('enter a number: ')
num2 =  input('enter a number: ')

print(num1 + num2)
print(int(num1) + int(num2))


#DATA TYPES
# strings
#int(1,2,3,4), float/decimal (0.2) (number)

#string 'hello', "cookie" => "hellocookie"
#string '10', "20" =>  "1020"
#math operators (+,-,*,**,/,//,%)
# tip calculater
food_amount = float(input('Enter food amount $: '))
tip_percentage = float(input('Enter your tip percentage %: '))/100
tip_amount = food_amount * tip_percentage
print(tip_amount)
# total  food_amount + tip_amount
total = food_amount + tip_amount
print('-----------------------------------')
print(f'🥗 Food Amount: ${food_amount}')
print(f'⚖ Tip Amount:  ${tip_amount}')
print('\n')
print(f'💰 Total Amount: ${total}')
print('------------------------------------')
print('$'+ str(total))


# string formating

print("-------------------")


# testing your code / unit tests
def calculateFoodTotal(food_amount, tip_percentage):
  tip_amount = food_amount * (tip_percentage/100)
  total = food_amount + tip_amount
  print(f'🥗 Food amount: ${food_amount}')
  print(f'⚖ Tip Amount: ${tip_amount}')
  print(f'💰 Total Amount: ${total}')
  return total
print('_________________________________________')



def sum(a: int, b: int )-> int:
  return a+b

print(sum(10,30))


def test_sum():
  assert sum(1,2) == 3, "sum(1,2) does not return 3 like it should"
  assert sum(-20, 20) == 0
  assert sum(20,20) == 40
  assert sum(560, 780) == 1340
  print('sum function: All Tests passed (2/2)')
test_sum()

def test_calulate_food_total():
  assert calculateFoodTotal(100, 20) == 120

test_calulate_food_total()








