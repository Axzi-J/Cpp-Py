""" print("hello world")

float_one = 3.33
float_two = 10 / 3
print(float_one)
print(float_two) """


""" var = input("input value: ")
var2 = int(var)

if var2 == 69:
    print("*Nice*")
else :
    print("you can do better than that")
    var = input("input value: ")
    var2 = int(var)
    if var2 == 69:
        print("*Nice*")
    else:
        print("nope, still not good enough, you don't get another chance tho")



if var2 - 420 == 0:
    print("aah, I see what you did there, nice one") """
""" 
x=0
while x <= 5:
    print(x)
    x = x + 1

var3 = len("fore")

print(var3) """

Names = ["Jonas", "Kasper", "Tobias"]


cars = ["Ford", "Volvo", "BMW"]

print("What car do you want?")

print("These are your options")
for x in cars:
    print(x)
var4= int(input("give me a number between 1 and 3: "))
wearegood = var4-1>= len(cars)
if wearegood:
    print("alright, you sneaky bastard, I'll give you an extra option just for you")
    cars.append("Honda")

if wearegood:
    print("boy you ain't playing around, ight, another it is")
    cars.append("Citröen")
if wearegood:
    print("Enough")
            


x = cars[var4-1]
print(x)

if x == "BMW":
    print("just fyi, you have a turn signal")
elif x == "Volvo":
    print("A russian eh?")
elif x == "Ford":
    print("Harrison, I presume?")
elif x=="Honda":
    print("alright", cars[3],  "it is")
else:
    print("alright", cars[4],  "it is")