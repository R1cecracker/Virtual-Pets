from random import randint

class Pet:
    def __init__(self, pet_name):
        self.name = pet_name
        self.age = 0
        self.hunger = 5
        self.boredom = 3
        self.sleepiness = 3
        self.dead = False

    def __str__(self):
        string = f"""Name: {self.name}
Age: {self.age}
Hunger: {"•" * self.hunger}
Boredom: {"•" * self.boredom}
Sleepiness: {"•" * self.sleepiness}
Dead? {self.dead}
"""
        return string

    def feed(self):
        if self.dead:
            return
        self.hunger = self.hunger - 4
        if self.hunger < -1:
            self.hunger = -1
        
    def play(self):
        if self.dead:
            return
        self.boredom = self.boredom - 4
        if self.boredom < -1:
            self.boredom = -1
    
    def rest(self):
        if self.dead:
            return
        self.sleepiness = self.sleepiness - 6
        if self.sleepiness < -1:
            self.sleepiness = -1

    def check_dead(self):
        if self.boredom == 10 or self.age >= randint(15,20) or self.hunger == 10 or self.sleepiness == 10:
            self.dead = True

    def wait(self):
        if self.dead:
            return
        self.age += 1
        self.hunger += 1
        self.boredom += 1
        self.sleepiness += 1

        if self.hunger > 10:
            self.hunger = 10
        if self.boredom > 10:
            self.boredom = 10
        if self.sleepiness > 10:
            self.sleepiness = 10
        self.check_dead()

name = input("What would you like to name your pet? ")
pet = Pet(name)
print(pet)

action = input("What would you like to do? (feed/play/rest/wait) ")
while action != "exit":
    if action == "feed":
        pet.feed()
        pet.wait()
        print(pet)
        action = input("What would you like to do? (feed/play/rest/wait) ")
    elif action == "play":
        pet.play()
        pet.wait()
        print(pet)
        action = input("What would you like to do? (feed/play/rest/wait) ")
    elif action == "rest":
        pet.rest()
        pet.wait()
        print(pet)
        action = input("What would you like to do? (feed/play/rest/wait) ")
    elif action == "wait":
        pet.wait()
        print(pet)
        action = input("What would you like to do? (feed/play/rest/wait) ")
    else:
        print("Invalid action. Please choose 'feed', 'play', or 'rest'.")
        action = input("What would you like to do? (feed/play/rest/wait) ")

####----Task 1----####
#Set up your pet with the following attributes:
#name (make this mandatory), age (default:0), hunger (default: 5), boredom (default:3), sleepiness(default:3)

####----Task 2----####
#instantiate your pet object with the name of your choice

####----Task 3----#### 
# We need to add the following methods to our Virtual Pet:
# 1. Feed - which will reduce hunger by 3
# use a selection to make sure if hunger goes below zero it gets reset to 0 (we don’t want any negative numbers.)
# 2. Play - which will reduce boredom by 3
# 3. Sleep - which will reduce sleepiness by 5
# 4. Wait - which will increase age, and increase hunger, boredom and sleepiness
# 5. Is_dead - which will check to see if the Pet has hit the thresholds we have set as the
# maximum possible hunger, boredom and sleepiness

###----Task 4----####
# Make a new method called check_death() that checks when a pet dies.
# These are the conditions I have chosen to use to determine if the pet should be dead.
# (Note: you can change these to make your pet harder or easier to keep alive)
    # ● Boredom is at 10
    # ● Sleepiness is at 10
    # ● Hunger is at 10
    # ● Age is at a random age between 15 and 20 or more

#Go to page 9 of the tutorial to learn how to make the mainline (https://classroom.google.com/w/NzE2NTQ0NzA2MTYx/t/all)