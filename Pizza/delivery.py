class Delivery:
    def __init__(self, num_of_person, pizza_list):
        # self.index = index
        self.ingredients = set()
        self.num_of_person = num_of_person
        self.num_of_pizza = len(pizza_list)
        self.pizzas = pizza_list
        for pizza in self.pizzas:
            self.ingredients.update(pizza.get_ingredients())
        
        if self.num_of_person != len(self.pizzas):
            raise Exception("Number of people {} not equal to numer of pizzas {}".\
                format(self.num_of_person, len(self.pizzas)))


    def get_pizzas(self):
        return self.pizzas
    
    def get_num_of_pizzas(self):
        return len(self.pizzas)

    def get_num_of_person(self):
        return self.num_of_person

    def get_ingredients(self):
        return self.ingredients
    
    def get_num_of_ingredients(self):
        return len(self.ingredients)
