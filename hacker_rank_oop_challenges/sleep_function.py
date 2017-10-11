def sleep(name):
    print("{} sleeps for 8 hours".format(name))


favoriteFood = "meat"

def eat(name, food):
    print("{} eats {}".format(name,food))
    if food == favoriteFood:
        print("YUM! {} wants more {}".format(name,food))


# Implement the Tiger class and its initializer, sleep and eat methods here
class Tiger(object):
    # Implement the initializer method here
    def __init__(self, name):
        self.name = name

    # Copy your sleep function here and modify it to work as a method
    def sleep(self):
        print("{} sleeps for 8 hours".format(self.name))

    # Copy your eat function here and modify it to work as a method
    def eat(self, food):
        favoriteFood = "meat"
        self.food = food
        print("{} eats {}".format(self.name, self.food))
        if self.food == favoriteFood:
            print("YUM! {} wants more {}".format(self.name,self.food))


# Implement the Bear class and its initializer, sleep and eat methods here
class Bear(object):
    #implament the initializer method here:
    def __init__(self,name):
        self.name = name
        self.favoriteFood = "fish"
    # sleep function for bear
    def sleep(self):
        #print the name of the bear along with hibernating for 4 months
        print("{} hibernates for 4 months".format(self.name))
    def eat(self,food):
        self.food = food
        print("{} eats {}".format(self.name,self.food))
        if self.food == self.favoriteFood:
            print("YUM! {} wants more {}".format(self.name, self.food))
