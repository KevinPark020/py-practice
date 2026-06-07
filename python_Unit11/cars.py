class Car:

    __slots__ = ["__VIN", "__make", "__model", "__year", "__miliege", "__fuel"]

    def __init__(self, vin, make, model, year):

        self.__VIN = vin
        self.__make = make
        self.__model = model
        self.__year = year
        self.__miliege = 0
        self.__fuel = 0

    def get_vin(self):

        return self.__VIN
    
    def get_make(self):

        return self.__make
    
    def get_model(self):

        return self.__model
    
    def get_year(self):

        return self.__year
    
    def get_miliege(self):

        return self.__miliege
    
    def get_fuel(self):

        return self.__fuel
    
    def filler_up(self, gallons):

        if gallons > 15:
            return None
        
        else:
            self.__fuel += gallons

    def drive(self, miles):

        if self.__fuel == 0:
            return None
        
        if self.__fuel - miles * (1/30) <= 0:
            return None

        self.__miliege += miles
        self.__fuel -= miles * (1/30)

    def __repr__(self):
        
        return "VIN: " + self.__VIN + "\nMAKE: " + self.__make + "\nMODEL: " + self.__model + "\nYEAR: " + str(self.__year) + "\nMILEGE: " + str(self.__miliege) + "\nFUEL: " + str(self.__fuel)

    def __str__(self):
        
        return "VIN: " + self.__VIN + " MAKE: " + self.__make + " MODEL: " + self.__model
    
    def __eq__(self, other):
        
        if self.__VIN == other.get_vin():

            return True
        
        return False
    
    def __lt__(self, other):
        
        if self.__VIN < other.get_vin():

            return True
        
        return False
    
    def __le__(self, other):
        
        if self.__VIN <= other.get_vin():

            return True
        
        return False
    
    def __gt__(self, other):
        
        if self.__VIN >= other.get_vin():

            return True
        
        return False
    
    def __ge__(self, other):
        
        if self.__VIN > other.get_vin():

            return True
        
        return False
    
    def __hash__(self):
        
        return hash(self.__VIN)


def print_cars(car):

    print("VIN: " + car.get_vin())
    print("MAKE: " + car.get_make())
    print("MODEL: " + car.get_model())
    print("YEAR: " + str(car.get_year()))
    print("MILEGE: " + str(car.get_miliege()))
    print("FUEL: " + str(car.get_fuel()))

        
        