# Implement the Animal superclass here
# Hint: Copy your Tiger class from Problem 4 and modify it to be more general
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


# Implement the Tiger class here as a subclass of Animal
# Hint: Implement the initializer method only
class Tiger(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "meat")


# Implement the Bear class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Bear(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "fish")
    def sleep(self):
        #print the name of the bear along with hibernating for 4 months
        print("{} hibernates for 4 months".format(self.name))

class Unicorn(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "marshmallows")
    def sleep(self):
        print("{} sleeps in a cloud".format(self.name))
