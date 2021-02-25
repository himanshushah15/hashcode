import io 

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x 
    
    def get_y(self):
        return self.__y

    def get_point(self):
        return [self.__x, self.__y]

    def set_x(self, x):
         self.__x = x
    
    def set_y(self, y):
         self.__y = y


class Task: 
    __assembly_point_list = []

    def __init__(self, score , num_of_point):
        self.__score = score
        self.__num_of_points = num_of_point
        
    def get_score(self):
        return self.__score 
    
    def get_num_of_points(self):
        return self.__num_of_points

    def get_assembly_point_list(self):
        return self.__assembly_point_list
    
    def set_assembly_point_list(self, point):
         self.__assembly_point_list.append(point) 
    
    

#read the input file 
input_file = open("problems/a_example.txt")

# parse the num of pizza and team details from the first line 
temp = input_file.readline()
temp_list = temp.split()
W = int(temp_list[0])
H = int(temp_list[1])
R = int(temp_list[2])
M = int(temp_list[3])
T = int(temp_list[4])
L = int(temp_list[5])

# now get the pizza information and store in the pizza class
mount_point_list = []
for mount_points in range(M):
    temp = input_file.readline()
    temp_list = temp.split()
    p = Point(temp_list[0], temp_list[1])
    mount_point_list.append(p)

task_list = []
for task in range(T):
    temp = input_file.readline()
    temp_list = temp.split()
    t = Task(temp_list[0], temp_list[1])
    temp = input_file.readline() 
    print(str(temp))
    temp_list = temp.split()
    print(temp_list)
    for task_points in range(int(t.get_num_of_points())):
        assembly_point = Point(temp_list[task_points*2], temp_list[task_points*2 + 1])
        t.set_assembly_point_list(assembly_point)
    task_list.append(t)
  
#close the file and print the number of pizzas parsed
input_file.close()

for task in task_list:
    p = task.get_assembly_point_list()
    for point in p: 
        print(point.get_point())