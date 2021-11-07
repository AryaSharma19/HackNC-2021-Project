


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
    #greet()                                                            ARYA
    #tillage()                                                             ARYA
    allocating()
    

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
    print(f"*description needed*")
    farmsize = int(input("How large do you want your farm to be? (Enter a whole number): "))

def soiltype() -> None: 
    #global soil                                                    ARYA
    #soil: int = randint(1,4)                                       ARYA

    print("You have the soil type ")


def allocating() -> None:
    """allocating"""
    print(f"Out of your total acerage ({farmsize}), how many acres do you want to allocate to:")
    global ssize 
    check: bool = False
    while check == False:
        a: float = float(input("Soybeans? (Enter a whole number)"))
        if farmsize >= a:
            ssize = a
            check = True
        else:
            print("Please enter a number that does not exceed your total farm acerage.")
    check = False
    global psize
    while check == False:
        b: float = float(input("Peanuts? (Enter a whole number)"))
        if farmsize >= b + ssize:
            psize = b
            check = True
        else:
            print("Please enter a number that does not exceed your total farm acerage.")
    check = False
    global csize 
    while check == False:
        c: float = float(input("Cotton? (Enter a whole number)"))
        if farmsize >= ssize + psize + c:
            csize = c
            check = True
        else:
            print("Please enter a number that does not exceed your total farm acerage.")
    check = False 
    global crsize
    while check == False:
        d: float = float(input("Corn? (Enter a whole number)"))
        if farmsize == ssize + psize + csize + d:
            crsize = d
            check = True
        else:
            print("Please enter a number that meets but does not exceed your total farm acerage.")

    

def seeding() -> None:
    """seeding"""
    print()

def watering1() -> None:
    """watering1"""
    global moisture
    w: int = int(input("On a scale of 1-4 with 1 being the most and 4 being the least, how much water do you want to add: "))
    check: bool = False
    while check == False:
        if 1<=w<=4:
            moisture = w
            check = True
        else:
            w = int(input("Please enter a number between 1-4: "))


def fertilizer() -> None:
    """fertilizer"""

def watering2() -> None:
    """watering2"""
    global moisture
    w: int = int(input("On a scale of 1-4 with 1 being the most and 4 being the least, how much water do you want to add: "))
    check: bool = False
    while check == False:
        if 1<=w<=4:
            moisture = w
            check = True
        else:
            w = int(input("Please enter a number between 1-4: "))

def pesticide() -> None:
    """pesticide"""

def weather() -> None:
    """weather"""
    #global soil                                                        ARYA
    #soil: int = randint(1,4)                                           ARYA

def watering3() -> None:
    """watering3"""
    global moisture
    w: int = int(input("On a scale of 1-4 with 1 being the most and 4 being the least, how much water do you want to add: "))
    check: bool = False
    while check == False:
        if 1<=w<=4:
            moisture = w
            check = True
        else:
            w = int(input("Please enter a number between 1-4: "))

def harvest() -> None:
    """harvest"""


if __name__ == "__main__":
    main()