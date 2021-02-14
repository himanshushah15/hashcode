from pizza import Pizza
from delivery import Delivery
from input_handler import pizza_list, T2, T3, T4


# Global Defines
D4 = 0
D3 = 0
D2 = 0

T4_left = T4 - D4
T3_left = T3 - D3
T2_left = T2 - D2

num_of_pizza = len(pizza_list)
num_pizza_left = num_of_pizza - 4 * D4 - 3 * D3 - 2 * D2

pizza_index = 0

isDelivery_T4 = True
isDelivery_T3 = True
isDelivery_T2 = True

delivery_T2_list = []
delivery_T3_list = []
delivery_T4_list = []

# Global Methods

def remove_choosen_pizza(left_pizza_list, tem_pizza_list):
    for pizza in tem_pizza_list:
        left_pizza_list.remove(pizza)

pizza_list.sort(key=lambda piz: piz.get_number_of_ingredients(), reverse=True)


# for pizza in pizza_list:
#     print(pizza.get_ingredients())

while True:
    #Look for the biggest team we can deliver
    if min(T4_left, int(num_pizza_left / 4)) > 0: # biggest team is a T4
        isDelivery_T4 = True
        temp_pizza_list_4 = pizza_list[pizza_index : pizza_index + 4]
        temp_delivery_T4 = Delivery(4, temp_pizza_list_4)

        for pizza in temp_pizza_list_4:
            temp_pizza_list_3 = temp_pizza_list_4[:]
            temp_pizza_list_3.remove(pizza)
            temp_delivery_T3 = Delivery(3, temp_pizza_list_3)
            if(temp_delivery_T3.get_num_of_ingredients() >= temp_delivery_T4.get_num_of_ingredients() and T3_left > 0):
                isDelivery_T4 = False
                isDelivery_T3 = True

                for pizza in temp_pizza_list_3:
                    temp_pizza_list_2 = temp_pizza_list_3[:]
                    temp_pizza_list_2.remove(pizza)
                    temp_delivery_T2 = Delivery(2, temp_pizza_list_2)
                    if(temp_delivery_T2.get_num_of_ingredients() >= temp_delivery_T3.get_num_of_ingredients() and T2_left >0):
                        isDelivery_T3 = False
                        T2_left -= 1
                        num_pizza_left -= 2
                        delivery_T2_list.append(temp_delivery_T2)
                        remove_choosen_pizza(pizza_list, temp_pizza_list_2)
                        D2 += 1
                        break

                if isDelivery_T3:
                    T3_left -= 1
                    num_pizza_left -= 3
                    delivery_T3_list.append(temp_delivery_T3)
                    remove_choosen_pizza(pizza_list, temp_pizza_list_3)
                    D3 += 1
                    break
    
        if isDelivery_T4:
            T4_left -= 1
            num_pizza_left -= 4 
            delivery_T4_list.append(temp_delivery_T4)
            for pizza in temp_pizza_list_4:
                print(pizza.get_ingredients())
            remove_choosen_pizza(pizza_list, temp_pizza_list_4)
            D4 += 1

    elif min(T3_left, int(num_pizza_left / 3)) > 0: # biggest team is a T3
        isDelivery_T3 = True
        temp_pizza_list_3 = pizza_list[pizza_index : pizza_index + 3]
        temp_delivery_T3 = Delivery(3, temp_pizza_list_3)

        for pizza in temp_pizza_list_3:
            temp_pizza_list_2 = temp_pizza_list_3[:]
            temp_pizza_list_2.remove(pizza)
            temp_delivery_T2 = Delivery(2, temp_pizza_list_2)
            if(temp_delivery_T2.get_num_of_ingredients() >= temp_delivery_T2.get_num_of_ingredients() and T2_left > 0):
                isDelivery_T3 = False
                T2_left -= 1
                num_pizza_left -= 2
                delivery_T2_list.append(temp_delivery_T2)
                remove_choosen_pizza(pizza_list, temp_pizza_list_2)
                D2 += 1
                break

        if isDelivery_T3:
            T3_left -= 1
            num_pizza_left -= 3
            delivery_T3_list.append(temp_delivery_T3)
            remove_choosen_pizza(pizza_list, temp_pizza_list_3)
            D3 += 1

    elif min(T2_left, int(num_pizza_left / 2)) > 0: # biggest team is a T2
        temp_pizza_list_2 = pizza_list[pizza_index : pizza_index + 2]
        temp_delivery_T2 = Delivery(2, temp_pizza_list_2)
        T2_left -= 1
        num_pizza_left -= 2
        delivery_T2_list.append(temp_delivery_T2)
        remove_choosen_pizza(pizza_list, temp_pizza_list_2)
        D2 += 1

    else:
        print("no delivery any more")
        break

D = D4 + D3 + D2

print('D', D, 'D2', D2, 'D3', D3, 'D4', D4)

score_T2 = 0
score_T3 = 0
score_T4 = 0

for delivery in delivery_T2_list:
    score_T2 += delivery.get_num_of_ingredients() ** 2

for delivery in delivery_T3_list:
    score_T3 += delivery.get_num_of_ingredients() ** 2

for delivery in delivery_T4_list:
    score_T4 += delivery.get_num_of_ingredients() ** 2

score = score_T2 + score_T3 + score_T4
print('score', score, 'score_T2', score_T2, 'score_T3', score_T3, 'score_T4', score_T4)