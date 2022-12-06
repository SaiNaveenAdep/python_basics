## function with Multipule Arguments ##
def greeting(greet,name):
  '''
  greating takes in 2 Arguments, greet & name and it greet the user
  >> greeting('aloha', 'Naveen')
  '''
  print(f'Hey!🤞 {greet} {name}!')


greeting('aloha','Naveen')

def calculateFoodTotal(food_amount, tip_percentage):
  tip_amount = food_amount * (tip_percentage/100)
  total = food_amount + tip_amount
  print(f'🥗 Food amount: ${food_amount}')
  print(f'⚖ Tip Amount: ${tip_amount}')
  print(f'💰 Total Amount: ${total}')
  return total
print('_________________________________________')
calculateFoodTotal(food_amount=100,tip_percentage=10)
print('_______________________________')
print()
calculateFoodTotal(500,20)

print("------------------")
def climate(weather: str) -> None: # its is using for not using return statement
  if weather == 'rain':
    print("it's raining today:☔")
  elif weather == 'sunny':
    print("It's sunny today: ☀")
  elif weather == 'cloudy':
    print("It's cloudy today: ☁")
  elif weather == 'tunderstome':
    print("It's tunderstome today: 🌪")
  else:
    print("Plese enter how was the weather Today")

climate("sunny")


def sum(a: int, b: int )-> int:
  return a+b

print(sum(10,30))


