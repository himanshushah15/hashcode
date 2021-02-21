class Pizza:

    def __init__(self, index, ingredients_list):
        self.index = index
        self.num_of_ingredients = len(ingredients_list)
        self.ingredients = ingredients_list

    def get_ingredients(self):
        return self.ingredients
    
    def get_index(self):
        return self.index

    def get_num_of_ingredients(self):
        return(len(self.ingredients))


# def main():
#     pizza = Pizza(0, ["Onion", "Tomato", "Mozarella"])
#     print(pizza.get_index())
#     print(pizza.get_ingredients())

# if __name__ == "__main__":
#     main()