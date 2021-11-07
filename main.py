


#tillage-how many acres   limit: 100


# NC only, choice 4 crops soybeans, peanuts, cotton, corn
#if they allocate more land than they originally had, go back to beginning




# seeding, 
#how dense do you want the corn, soy beans, etc....
#if they overseed reduce yield



# application, 
#1st watering
#fertilizer
#2 watering
#pesticides
#3 watering
#weather - muktha
#allocation, watering - arya
#soiltype - karen
#fertilizer, pesticides - marcus




# harvest
#return yield percentage 
#return profit
from random import randint

player: str = ""
totalprof: float = 0.0
totalyield: float = 0.0
balance: float = 25000.0
farmsize: int = 0
ssize: float = 0.0
psize: float = 0.0
csize: float = 0.0
crsize: float = 0.0
soil: int = 0
soiltype: int = 0 #1-brand new soil; 2-used soil; 3- extremely unhealthy
weather: int = 0
moisture: int = 0 #int 1 - 4 (best - worst)


def main() -> None:
    """Entrypoint into the program"""
    greet()
    tillage()
    

def greet() -> None:
    """Intro to the game"""
    global player 
    player = str(input("Player name: ")) 
    print(f"Welcome {player}!") 
    print("This is ArgiLife, a farming simulation. In this game, you will be a North Carolinian farmer!")
    print("Your goal is to maximize yield and profit for the end-of-year farmer's market.")
    print(f"Depending on your decisions, your profit will change. Your initial balance to use on supplies and tools is ${balance}")

def tillage() -> None:
    """how many acres"""
    global farmsize
    print("*description needed*")
    farmsize = int(input("How large do you want your farm to be? (Enter a whole number): "))

def soil_type() -> None: 
    """Determines soil type for the game."""
    print("Good farmers pay attention to their soil type.")
    global soiltype
    soiltype = randint(1,3)
    if soiltype == 1:
        print("You have fresh, brand new soil.")
    elif soiltype == 2:
        print("Your soil was used last season to cultivate other crops.")
    else:
        print("Oh no, your soil is extremely unhealthy!")


def allocating() -> None:
    """allocating"""
    global ssize
    global psize
    global csize
    global crsize
    

def seeding() -> None:
    """seeding"""
    print()

def watering1() -> None:
    """watering1"""

def fertilizer() -> None:
    """fertilizer"""

def watering2() -> None:
    """watering2"""

def pesticide() -> None:
    """pesticide"""

def weather() -> None:
    """weather"""
    global soil
    soil = randint(1,4) #1-rainy 2-perfect 3-sunny 4-lightning
    if soil == 1:
        global moisture
        moisture -= 1
        print("The weather is extremely rainy! Your crops are getting flooded.")
    elif soil == 2:
        print("The weather is absolutely perfect! Your crops are thriving.")
    elif soil == 3: 
        global moisture
        moisture -= 1
        print("The weather is extremely sunny! Your crops are getting dry.")
    elif soil == 4:
        print("The weather is extremely stormy!")
        print("...Oh no! All your crops got destroyed by lightning.")
        main()

def watering3() -> None:
    """watering3"""

def harvest() -> None:
    """harvest"""


if __name__ == "__main__":
    main()

