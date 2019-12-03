import math

def main():
    f = open("input", "r").readlines() # Read in file

    masses = [] # Create array to hold all masses
    totalFuelRequirement = 0

    for l in f:
        masses.append(int(l)) # Append to masses array (convert all masses to integers)

    for i in masses:
        # Get total fuel requirement - divide each mass by 3, round it down and take away 2
        totalFuelRequirement += math.floor((i / 3)) - 2 

    print(totalFuelRequirement)

if __name__ == "__main__":
    main()