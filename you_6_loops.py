# loops

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

print("Diferent between using break before print statement and after the print statement")
names = ['naveen', 'adep', 'hare', 'krishna','mohan']
for name in names:
    print(name)
    if name == 'hare':
        break
print("--------------------------------------------------")

print("using the break statement before the print statement")
print("which give you a out put till tirupathi")
print('\n')
places = ['vemulawada', 'vrindavan', 'mayapur', 'tirupathi', 'ayodhya']

for place in places:
    print(place)
    if place == 'tirupathi':
        break
print("---------------------------------------------------------")
print("using the break statement after the print statement")
print("which give you a out put till 'vrindavan' and exclude 'mayapur',")
print('\n')
for place in places:
    if place == 'mayapur':
        break
    print(place)
print("--------------------------------------")
print('\n')
for place in places:
    print(place)
    if place == 'ayodhya':
        break


vegitables = ['Brinjal', 'tomato', 'carrot', 'radiesh', 'cabage']

print("\n")
print("-------------------------------------")
print("\n")


countries1=['India', 'usa', 'uk','Australia', 'southafrica', 'Europe', 'France', 'Netherlands']
def world(countries1):
    while True:
        countries = input("Enter your country:")
        for country in countries:
            for countries_names_by_letters in country:
                print(countries_names_by_letters)
        if countries == 'India'.capitalize():
            print("i love india")
            break
        elif countries == 'usa':
            print("I love usa")
            break
        elif countries == 'uk' :
            print("I love uk")
            break
        elif countries == 'Australia' :
            print("I love Australia")
            break
        elif countries == 'southafrica' :
            print("I love southafrica")
            break
        elif countries == 'Europe' :
            print("I love Europe")
            break
    return countries1
world(" ")



#

