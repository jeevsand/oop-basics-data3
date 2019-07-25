#classes are the basis of oop - object oriented programming
#They are cookie cutters for objects.
#From classes you initalise individual instances of this class
#Classes hold methods (methods are functions that depend on instances of classes)
#Methods can only be called on instances of a class
class Animal ():
    def __init__(self, name, age): #constructor method runs everytime an instance is created
        #Properties of the animal
        self.name = name
        self.species = 'Lizard'
        self.age = age
        self.number_animal_eaten = 0

    #methods for class object - instances
    def sleep(self): #self refers to the instance if gets called upon- self populates the self with the instance
        return "zzz"

    def eat(self, food):
        self.number_animal_eaten += 1
        return "nom NOM nom NOM " + food

    def potty(self):
        return "....."


