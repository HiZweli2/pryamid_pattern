import logging

# Create a logger that will log everything that happens on the app to help with debugging
logging.basicConfig(
    filename='logFile.log',
    format="{asctime} - {levelname} - {message}",
    level = "NOTSET",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

logging.info("---------------------Starting App-----------------------")

# Get user input 
logging.info("Getting user symbol")
charLimit = 1
symbol = input("Enter a single digit or character: ")
while len(symbol) != charLimit:
    print("Invalid number of characters. Please enter a SINGLE character")
    symbol = input("Enter a single digit or character: ")
logging.info("User symbol: " + symbol)

# prompt user to choose a pattern 
logging.info("Getting pattern from user")
patternType = input("Enter pattern type ['clock' or 'pyramid']: ").lower()
while patternType != "clock" and patternType != "pyramid":
    patternType = input("Enter pattern type ['clock' or 'pyramid']: ").lower() 
logging.info("User pattern: " + patternType)

# prompt user for height of the chosen pattern 
logging.info("Getting pattern height from user")
validHeightInput = False
while validHeightInput == False:
    try:
        height = int(input("Enter height: ")) if patternType == "pyramid" else int(input("Enter odd number as height: "))
        validHeightInput = True
    except Exception as err:
        logging.error(err)
        print("Input is not a number") 
while height % 2 == 0 and patternType == "clock":
    try:
        height = int(input("Enter odd number as height: "))
    except Exception as err:
        logging.error(err)
        print("Input is not a number") 
logging.info("Pattern height: " + str(height))

#Creates pyramid pattern using given symbol/character
def buildPyramid(symbol,height): 
    logging.info("Now building pyramid")
    for x in range(height):
        i = x + 1
        j = 0
        while i < height:
            print(" ", end="")
            i = i + 1
            
        i = x + 1
        while j < i:
            print(symbol , end="")
            j = j + 1
        print("")
    pass


#Creates a sand clock shape using a given symbol/character
def buildClock(symbol,height):
    logging.info("Now building sand clock")
    width = height + 2
    amtOfSpace = 0
    reverse = False
    for x in range(height):
        i = 0
        j = 0  
        while j <  amtOfSpace:
            print(" ", end="")  
            j += 1

        while i <  width - (amtOfSpace * 2):
            print(symbol, end="")  
            i += 1

        if reverse == False:
            amtOfSpace += 2 if x == 0 else 1
        else:
            amtOfSpace -= 2 if x == (height -2)  else 1

        print("")

        if (width - amtOfSpace) * 2 == width - 1:
             reverse = True
             amtOfSpace -= 2
    pass

if patternType == "pyramid":
    buildPyramid(symbol,height)
elif patternType == "clock":
    buildClock(symbol,height)