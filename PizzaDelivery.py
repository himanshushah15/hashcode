from pizza import Pizza
from delivery import Delivery
#Hard Coded Input
num_of_pizza = 5
num_of_t2 = 1
num_of_t3 = 1
num_of_t4 = 1

pizza_list = []

pizza_list.append(Pizza(0, ["onion", "pepper","olive"]))
pizza_list.append(Pizza(1, ["mushroom", "tomato","basil"]))
pizza_list.append(Pizza(2, ["chicken", "mushroom","pepper"]))
pizza_list.append(Pizza(3, ["tomato", "mushroom","basil"]))
pizza_list.append(Pizza(4, ["chicken", "basil"]))

#Big Team Prioritized
left_pizza = num_of_pizza
num_of_D4 = min(num_of_t4, int(left_pizza / 4))

left_pizza = left_pizza - 4 * num_of_D4
num_of_D3 = min(num_of_t3, int(left_pizza / 3))

left_pizza = left_pizza - 3 * num_of_D3
num_of_D2 = min(num_of_t2, int(left_pizza / 2))

#Submission
D = num_of_D4 + num_of_D3 + num_of_D2
print(D, num_of_D4, num_of_D3, num_of_D2)

for index in range(num_of_D4)
    delivery_list.append(Delivery(4, ))