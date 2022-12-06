# BOOLEAN (True, False)
# IF THEN ELSE

# if withdrawal amount > balance:
#    don't allow withdraw
# else:
#     allow withdrawl

# Baby wather app
weather = 'rain'

if weather == 'rain':
    print("☔")
else:
    print('😃')

weather1 = input("How is the weather?")

if weather1 == 'rain':
  print("it's raining ☔")
elif weather1 == 'coudy':
  print("it's cloudy  ⛈")
elif weather1 == 'sunny':
  print("it's sunny  ☀")
elif weather1 == 'tunderstome':
  print("it's tunderstome ⛈")
else:
  print('😎')


# comparison operators (==, <, >, <=, >=)

# comparison operators (==, <, >, <=, >=)

score = float(input("Enter your score: "))

if score >=90:

  print("You are in A grade")

elif score >=80:
  print("you are in B grade")

elif score >=70:
  print("you are in c grade")

elif score >=60:
  print("you are in D grade")

elif score < 60:
  print("You are in F grade")

else:
  print(" you scored very low to give you a grade")

print("---------------------------------------")


# eiter a SUPER PASS  passing grade or a failing grade
# SUPER PASS > 100

score = 80
if score >=60 and score <= 100: # this is the regular way of writing the pythonic code
  print("passing grade")


#  we can write the python code in a simple manner
# Example for a simple code by not using the "and" boolean  key word
if 60 <= score <= 100: # pythonic way o fwriting the code
  print("passing grade")