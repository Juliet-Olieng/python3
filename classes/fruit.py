class Fruit:
    vitamin='vitamin C'
    def __init__(self,price,color,taste,name):
        self.price=price
        self.color=color
        self.taste=taste
        self.name=name
    def flavour_of_fruit(self):
        return f"{self.name} is {self.taste}"
    def market_sales(self):
        return f"the market sells {self.name} {self.price}"
    def discription_of_fruit(self):
        return f"{self.name} is{self.color}and usually taste{self.taste}"