
#Quiz
class House:
    def __init__(self, location, housetype, deal, price, year):
        self.location = location
        self.housetype = housetype
        self.deal = deal
        self.price=price
        self.year = year
    
    def showdetail(self):
        print(self.location, self.housetype, self.deal,\
            self.price, self.year)
houses = []
house1 = House("Gangnam","Apartment","Buy","10","2020")
house2 = House("Mapo","Officetel","Monthly","500/50","2005")
house3 = House("Songpa","Apartment","Buy","8","2010")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("there are {0} estates".format(len(houses)))
for h in houses:
    h.showdetail()

