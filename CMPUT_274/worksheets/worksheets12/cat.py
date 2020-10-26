from dog import Dog

class Cat(Dog):

    """
    def __init__(self, age=0, colour="brown", size="medium"):
        # override ?
        # overload != override

        # self point to that instance (being invoked)

        # obj is an instance of class, obj includes prop., attr., vars; class include func, template and
        # their body / def.

        # obj holds on the states / status (attrs. props), objs can have different states btw each other

        # objs share the same method of the class

        # dispatch (simple ex) -> invoke bark(), find the func from class

        # super(Cat, self).__init__(age=age, colour=colour, size=size)
        pass
    """

    @staticmethod
    def meow():
        print("meow")


a = Cat(age=1, colour="yellow")
print(a.colour)