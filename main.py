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
Age: {str(self.age)}
Hunger: {str(self.hunger)}
Boredom: {str(self.boredom)}
Sleepiness: {str(self.sleepiness)}
Dead? {str(self.dead)}
"""
        return string

    def feed(self):
        if self.dead:
            return
        self.hunger = self.hunger - 3
        if self.hunger < 0:
            self.hunger = 0
            self.hunger -= 3
        
    def play(self):
        if self.dead:
            return
        self.boredom = self.boredom - 3
        if self.boredom < 0:
            self.boredom = 0
            self.boredom -= 3
    
    def rest(self):
        if self.dead:
            return
        self.sleepiness = self.sleepiness - 5
        if self.sleepiness < 0:
            self.sleepiness = 0
            self.sleepiness -= 5

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

    def dead(self):
        if self.boredom == 10 and self.age >= 15 and self.hunger == 10 and self.sleepiness == 10:
            self.dead = True

name = input("What would you like to name your pet? ")
pet = Pet(name)
print(name)

action = input("What would you like to do? (feed/play/rest/wait/exit) ")
while action != "exit":
    if action == "feed":
        pet.feed()
    elif action == "play":
        pet.play()
    elif action == "rest":
        pet.rest()
    elif action == "wait":
        pet.wait()
    elif action == "check":
        print(pet)
    elif action == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid action. Please choose 'feed', 'play', or 'rest'.")
        action = input("What would you like to do? (feed/play/rest/wait/exit) ")

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