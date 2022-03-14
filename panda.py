#coding:utf-8

class Panda:
    def __init__(self, name, age):
        assert name.isalnum(), " Attribut 'name' : doit etre alphnumerique (a-z, A-Z, 1-9)"
        assert len(name)>3 and len(name)<25, "Attribut 'name' : nombre de caractère > 3 et < 25"
        assert isinstance(age, int)," Attribut 'age' : doit etre entier (instance de 'int')"
        assert age >0 and age <= 100, "Attribut 'age' : nombre > 0 et >= 100 "
        self.name = name
        self.age = age
        self.hunger = 50


    def __str__(self):
        return f"[Name: {self.name} / : Age :{self.age} / Faim : {self.hunger}/100]"


    def eat(self,food_points):
        if self.hunger >100
