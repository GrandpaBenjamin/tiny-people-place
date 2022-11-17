from tiny_people_sim.Family import FamilySystem

class Entity:
    def __init__(self,name,description,age,lifespan,familySystem):
        self.name = name
        self.description = description
        self.age = age
        self.lifespan = lifespan
        self.familySystem = familySystem
    
    def reproduce(self):
        pass

class Human(Entity):
    def __init__(self,name,description,age,lifespan,familySystem):
        super().__init__(name,description,age,lifespan,familySystem)