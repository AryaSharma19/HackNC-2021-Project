


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
    print("*description needed*")
    print(f"Your current balance is: {balance}")

def tillage() -> None:
    """how many acres"""
    global farmsize
    print("*description needed*")
    farmsize = int(input("How large do you want your farm to be? (Enter a whole number): "))

def soiltype() -> None: 
    global soil
    soil: int = randint(1,4)

    print("You have the soil type ")


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
#fertilizer should have a positive effect the soil variable.  
#fertilizer should have a negative effect on balance. needs a price
    global soil
    global balance
    fprice: float = 0.0
    print("The crops have sprouted and are leafing out. If more nutrients are needed to improve yield it would be a good time add fertilizer. Fertilizer is *cost needed* per unit.")
    fertilizer = int(input("Would you like to fertilize the soil? (Choose a whole number between 0-2): "))
    if fertilizer == 2:
        balance -= 2*fprice
        if soil < 2:
            soil += 2
        else:
            soil = 3
    if fertilizer == 1:
        balance -= fprice
        if soil < 3:
            soil += 1
        else:
            soil = 3
    
    """fertilizer"""

def watering2() -> None:
    """watering2"""

def pesticide() -> None:
#pesticide should increase yield
#pesticide should reduce balance
#may need a global boolean variable for a multiplier on yield during harvest.
    global balance
    pestprice: float = 0.0
    print("When scouting the crops you notice some evidence of damage from insects.  Pesticide treatment could reduce the damage and increase your yield. Pesticide treatment is *cost needed*.")
    pesttreatment = bool(input("Do you get a pesticide treatment your fields?"))
    if pesttreatment:
        balance -= pestprice
    """pesticide"""

def weather() -> None:
    """weather"""
    global soil
    soil: int = randint(1,4)

def watering3() -> None:
    """watering3"""

def harvest() -> None:
    """harvest"""


if __name__ == "__main__":
    main()