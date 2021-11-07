


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
    """fertilizer"""

def watering2() -> None:
    """watering2"""

def pesticide() -> None:
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