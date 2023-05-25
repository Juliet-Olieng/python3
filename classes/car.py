class Car:
    wheels=4
    def __init__(self,make,model,color,speed,year):
        self.make=make
        self.speed=speed
        self.model=model
        self.color=color
        self.year=year
    def age_of_car(self):
        return f'the car is {2023-self.year} years'
    def car_details(self):
        return f'the car is a {self.make} {self.model} and its{self.color}in color '
    def distance_covered(self,time):
        return f'the car covered a distance of {self.speed*time} km'
    



        
    


    
