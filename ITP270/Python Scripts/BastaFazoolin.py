# Creating the Menu class
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = {}
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"{self.name} menu available from {self.start_time} to {self.end_time}"

    def calculate_bill(self, purchased_items):
        self.purchased_items = purchased_items
        total = []

        for item in purchased_items:
            for food, price in self.items.items():
                if item == food:
                    total.append(price)
        return sum(total)

# Creating dictionaries of menu items
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
earlybird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
dinner_items = {'crostini w/ eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu':19.50 , 'mushroom ravioli(vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
kids_items = {'chicken nuggets': 6.50, 'fusilli w/ wild mushrooms': 12.00, 'apple juice': 3.00}
arepa_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

# Creating instances of the Menu class
brunch = Menu("Brunch", brunch_items, start_time=11, end_time=16)

early_bird = Menu("Early-bird Dinner", earlybird_items, start_time =15, end_time=18)

dinner = Menu("Dinner", dinner_items, start_time=17, end_time=23)

kids = Menu("Kids", kids_items, start_time=11, end_time=19)

arepas = Menu("Arepas", arepa_items, start_time=10, end_time=17)
# Testing the __repr__ function 
#print(brunch)
#print(early_bird)
#print(dinner)
#print(kids)

#print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))

# Creating the Franchise class
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    
    def __repr__(self, address):
        return "Come find us at {address}!".format(address=self.address)
    
    def available_menus(self, time):
        self.time = time
        current_menu = []

        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                for i in menu.items:
                    current_menu.append(i)
        return current_menu

# Creating instances of the Franchise class
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
#print(new_installment.available_menus(12))
#print(new_installment.available_menus(17))

arepas_place = Franchise("189 Fitzgerald Avenue", [arepa_items])
#print(arepas_place.available_menus(12))

# Creating the Business class
class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

# Making instances of the business class
Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

Business("Take a' Arepa", [arepas_place])