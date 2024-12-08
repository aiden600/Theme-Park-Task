class Attraction:
    def __init__(self, name, capacity):
        self.__name = name
        self.__capacity = capacity

    def get_details(self):
        print(f"Attraction: {self.__name}, Capacity: {self.__capacity}")

    def start(self):
        print("The attraction is starting")

class ThrillRide(Attraction):
    def __init__(self, name, capacity, min_height):
        super().__init__(name, capacity)
        self.__min_height = min_height

    def start(self):
        print(f"Thrill ride {self._Attraction__name} is now starting. Hold on tight!")

    def is_eligible(self, height):
        if height < self.__min_height:
            print("You are not eligible for this ride")
            return False
        else:
            print("You are eligible for this ride")
            return True

class FamilyRide(Attraction):
    def __init__(self, name, capacity, min_age):
        super().__init__(name, capacity)
        self.__min_age = min_age

    def start(self):
        print(f"Family ride {self._Attraction__name} is now starting. Enjoy the fun!")

    def is_eligible(self, age):
        if age < self.__min_age:
            print("You do not meet the age requirement")
            return False
        else:
            print("You are eligible for this ride")
            return True

class Staff:
    def __init__(self, name, role):
        self.__name = name
        self.__role = role

    def work(self):
        print(f"Staff {self.__name} is performing their role: {self.__role}")

class Visitor:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    def ride(self, attraction):
        if isinstance(attraction, ThrillRide):
            if attraction.is_eligible(self.__height):
                attraction.start()
        elif isinstance(attraction, FamilyRide):
            if attraction.is_eligible(self.__age):
                attraction.start()

Dragon = ThrillRide("Dragon", 20, 140)
Merry = FamilyRide("Merry", 30, 4)
Tonye = Visitor("Tonye", 1, 130)

Tonye.ride(Dragon)
Tonye.ride(Merry)
