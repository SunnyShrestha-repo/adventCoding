#Sunny Shrestha

# Fuel required to launch a given module is based on its mass.
# Specifically, to find the fuel required for a module, take its mass,
# divide by three, round down, and subtract 2.


with open('input.txt', 'r') as puzzle_input:
    input = puzzle_input.readlines()
    totalFuel = 0
    for lines in input:
        result = False
        fuel = int(lines.rstrip())//3 - 2
        #print(fuel)
        totalFuel += fuel
        while result != True:
            if (fuel//3)-2 > 0:
                newfuel = (fuel//3)-2
                totalFuel += newfuel
                fuel = newfuel
                print("newfuel:", newfuel)
                print("total at this point:", totalFuel)
            else:
                result = True



print(totalFuel)
#at the end: 1609515
#at the top: 4833211
