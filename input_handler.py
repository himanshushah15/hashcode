import io 
from pizza import Pizza

#read the input file 
input_file = open("Problems/2021/practice_problem/e_many_teams.in")

# parse the num of pizza and team details from the first line 
temp = input_file.readline()
temp_list = temp.split()
num_of_pizza = int(temp_list[0])
T2 = int(temp_list[1])
T3 = int(temp_list[2])
T4 = int(temp_list[3])

# now get the pizza information and store in the pizza class
pizza_list = []
for index in range(num_of_pizza):
    temp = input_file.readline()
    temp_list = temp.split()
    temp_list.remove(temp_list[0])
    pizza_list.append(Pizza(index, temp_list))

#close the file and print the number of pizzas parsed
input_file.close()
if (len(pizza_list) == num_of_pizza):
    print("parse successful. Parsed " + str(len(pizza_list)) + " pizzas")