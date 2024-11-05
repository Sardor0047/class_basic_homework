#Create a "Person" class
#Create an attribute "name" in the "Person" class
class Person :
    def __init__(self,name,age=None):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name