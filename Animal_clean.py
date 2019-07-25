class Animal():

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.alive = True

    def sleep(self):
        return "zzz"

    def eat(self, food):
        return "nom NOM nom NOM on" + food

    def potty(self):
        return "...."

    def shout_own_name(self):
        return "My name is" + self.name.upper() + "!!!"