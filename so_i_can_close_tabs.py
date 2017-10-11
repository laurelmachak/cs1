# Copy your Animal class here
class Animal(object):
    # implament initializer with name & favoriteFood as args
    def __init__(self, name, favoriteFood):
        self.name = name
        self.favoriteFood = favoriteFood

    # def sleep method
    def sleep(self):
        print("{} sleeps for 8 hours".format(self.name))

    #def eat method
    def eat(self,food):
        self.food = food
        print("{} eats {}".format(self.name,self.food))
        if self.food == self.favoriteFood:
            print("YUM! {} wants more {}".format(self.name, self.food))



# Copy your Tiger class here
class Tiger(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "meat")


# Copy your Bear class here
class Bear(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "fish")
    def sleep(self):
        #print the name of the bear along with hibernating for 4 months
        print("{} hibernates for 4 months".format(self.name))


# Implement the Unicorn class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Unicorn(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "marshmallows")
    def sleep(self):
        print("{} sleeps in a cloud".format(self.name))


# Implement the Giraffe class here as a subclass of Animal
# Hint: Implement the initializer method and override the eat method
class Giraffe(Animal):
    def __init__(self,name):
        Animal.__init__(self, name, "leaves")
    def eat(self, food):
        Animal(eat)


# Implement the Bee class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep and eat methods
class Bee(Animal):
    ...
