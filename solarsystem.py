class System:
    def __init__(self):
        self.bodies = []
    
    def add(self, celestial):
        if celestial in self.bodies:
            return
        self.bodies.append(celestial)

    def total_mass(self, number):
        mass = 0
        for m in number:
            mass += m
        return mass

class Body:
    def __init__(self, name, body_mass):
        self.name = name
        self.body_mass = body_mass

class Planet(Body):
    def __init__(self, name, body_mass, day, year):
        super().__init__(name, body_mass)
        self.day = day
        self.year = year

class Star(Body):
    def __init__(self, name, body_mass, star_type):
        super().__init__(name, body_mass)
        self.star_type = star_type

class Moon(Body):
    def __init__(self, name, body_mass, month, planet):
        super().__init__(name, body_mass)
        self.month = month
        self.planet = planet

earth = Planet('Earth', 100, 8760, 365)
print(earth.name)

sun = Star('Sun', 200, 'G-Type')
print(sun.star_type)

moon = Moon('Moon', 50, 27, 'Earth')
print(moon.planet)