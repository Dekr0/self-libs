animals = {'dog', 'cat', 'fish', 'snake'}
print("The contents of object {} are {}".format(id(animals), animals))

animals.remove("snake")
animals.update("bird")
print("The contents of object {} are {}".format(id(animals), animals))

alice_pets = {'dog', 'cat', 'rabbit', 'hamster'}
print("Alice could buy {} from Pets R Us".format(animals.intersection(alice_pets)))
