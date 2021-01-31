class Delivery:

    def __init__(self, num_of_person, pizza_list):
        # self.index = index
        self.num_of_person = num_of_person
        self.num_of_pizza = len(pizza_list)
        self.pizzas = pizza_list

    def get_pizzas(self):
        return self.pizzas
    
    # def get_index(self):
    #     return self.index

    def get_person(self):
        return self.num_of_person
