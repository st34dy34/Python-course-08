"""
class Car:
    def __init__(self,engine,wheels,color) -> None:
        self.engine = engine
        self.wheels = wheels
        self.color = color

    
    def start(self):
        print(f"Startuju na motoru {self.engine}")
    

    def respray(self,color):
        print(f"Sprejuju z barvy {self.color} na barvu {color}!")
        self.color = color

    def __str__(self):
        return f"engine: {self.engine}, wheels: {self.wheels}" 
        

c1 = Car("E1", 4, "black")
print(c1)
c1.respray("red")
"""

class City:
    def __init__(self,name,region,country,citizens) -> None:
        """
        :param name: name of city
        :param region: name of region
        :param country: name of country
        :param citizens: population of countr
        """
        self.name = name 
        self.region = region
        self.country = country
        self.citizens = citizens

    def __str__(self) -> str:
        return f"You live in {self.name}, a city in {self.region}, {self.country}. Current population is {self.citizens}"
    
    def ChangeCitizens(self):
        value = input("Kolik že má Brno obyvatel?")
        self.citizens = value
    
Brno = City("Brno","Jihomoravsky Kraj", "Czech Republic", 560230)
print(Brno)
Brno.ChangeCitizens()

print(Brno)


