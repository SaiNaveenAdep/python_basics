loops

fruits = ['Apple','Bananna', 'Orange', 'Grapes', 'watermelon']

for fruit in fruits:
    print(fruit)


vegitables = ['Brinjal', 'tomato', 'carrot', 'radiesh', 'cabage']

for veggies in vegitables:
    print("These are the following letters of vegitables:" + " "+ veggies)
    for letters in veggies:
        print(letters)


x = [1,2]
y = [0,9]
z = [7,5]
m = [8,0]

for i in x:
    for j in y:
        print(i,j)


name = "sainaveen"

for letters in name:
    print(letters)



cars = {'tata': 'harieer', 'honda': 'Civic', 'kia': 'seltoes', 'ford': 'enduvor'}
# print(cars.values())

for brand_name in cars.keys():
        print(brand_name)
print("--------------------------")
# break statement
bikes = ['honda', 'tvs', 'royalenfiled', 'ktm']

for bike_name in bikes:
        print(bike_name)
        if bike_name == 'tvs':
                break
print("-------------------")
fruits = ['apple', 'bananna', 'grapes', 'mango', 'gauva']

for fruit in fruits:
        print(fruit)
        if fruit == 'mango':
                break
print("-------------")

fashion = ['shirt', 'paint', 'shot', 'boxer']

for dresses in  fashion:
        if dresses == 'shot':
                break
        print(dresses)

print("--------------------------------")

# continue statement

pens = ['red', 'balck', 'green', 'blue']

for pen_colors in pens:
        if pen_colors == 'green':
                continue
        print(pen_colors)

print("-----------------------------")

# range ()


for phone in range(20):
        print(phone)


fruit1 = ['apple', 'bananna', 'grapes', 'mango', 'gauva']

for i in fruit1:
        for j in fruit1:
                print(i,j)



print("----------------")
for i in range(1,11):
        for j in range(1,11):
                print(i*j,end = ' ')
        print()
print("---------------------------")

for i in range(1,11):
        print(i)
        for j in range(1,11):
                print(i)
        print()