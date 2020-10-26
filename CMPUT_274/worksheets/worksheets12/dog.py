class Dog:

    def __init__(self, age=0, colour="brown", size="medium"):
        self.age = age
        self.colour = colour
        self.size = size
        self.desc()


    def __str__(self):
        return "%s dog" % (self.colour)

    def __repr__(self):
        return "Id<%s> %s dog" % (id(self), self.colour)

    def bark(self, level="loudly"):
        print("I am barking %s said the %s" % (level, self.colour))

    def desc(self):
        print("I am a %s dog, of age %s, of size %s" % (self.colour, self.age, self.size))

    def wag_tail(self):
        print("See my %s tail wagging slowly" % self.colour)
        

class Cat:

    def __init__(self, age=0, colour="brown", size="medium"):
        self.age = age
        self.colour = colour
        self.size = size
        self.desc()
    
    def __repr__(self):
        return "Id<%s> %s cat" % (id(self), self.colour)
    
    def bark(self, level="loudly"):
        print("I am barking %s said the %s" % (level, self.colour))
    
    def desc(self):
        print("I am a %s cat, of age %s, of size %s" % (self.colour, self.age, self.size))
    
    def meow(self):
        print("meow")
    
    def wag_tail(self):
        print("See my %s tail wagging slowly" % self.colour)