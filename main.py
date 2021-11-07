


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
pesttreament: bool = False


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
    print(f"*description needed*")
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
#pesticide should increase yield
#pesticide should reduce balance
#may need a global boolean variable for a multiplier on yield during harvest.
    global balance
    global pesttreament
    pestprice: float = 0.0
    print("When scouting the crops you notice some evidence of damage from insects.  Pesticide treatment could reduce the damage and increase your yield. Pesticide treatment is *cost needed*.")
    pesttreatment = bool(input("Do you get a pesticide treatment your fields?(true or false)"))
    if pesttreatment:
        balance -= pestprice
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

