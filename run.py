from oop_animal_class import *

# animal_1 = Animal() #creating 1 instance of class Animal
#
# # print (animal_1)
# # print (type(animal_1))
# print (animal_1.sleep())
# print (animal_1.eat('meat salad'))
# print (animal_1.potty())
#
# #Accessing properties of instance of animal
# print(animal_1.name)

# print(Animal().sleep())
animal_instance_ringo = Animal('ringo', 10)
animal_instance_hugo = Animal ('hugo', 2)

print(animal_instance_ringo)
print (animal_instance_ringo.name)


animal_instance_hugo.eat('chicken')
print(animal_instance_hugo.number_animal_eaten)
animal_instance_hugo.eat('salad')
animal_instance_hugo.eat('tacos')
print(animal_instance_hugo.number_animal_eaten)