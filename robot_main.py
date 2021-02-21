# W H R M T L 

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
    def __init__(self, task_index, score , num_of_point):
        self.__score = score
        self.__num_of_points = num_of_point
        self.__assembly_point_list = []
        self.__task_index = task_index
        
    def get_score(self):
        return self.__score 
    
    def get_num_of_points(self):
        return self.__num_of_points

    def get_assembly_point_list(self):
        return self.__assembly_point_list
    
    def set_assembly_point_list(self, point):
         self.__assembly_point_list.append(point) 

    def get_task_number(self):
        return self.__task_index


class Robot:
    def __init__(self, mount_point, tasks):
        self.__mount_point = mount_point
        self.__tasks = tasks 
        self.__move_list = ""
        self.__completed_tasks = []

    def get_move_list(self):
        return self.__move_list

    def get_tasks(self):
        return self.__tasks
    
    def get_completed_tasks(self):
        return self.__completed_tasks
    
    def get_mount_point_list(self):
        return self.__mount_point.get_point()
    
    def get_mount_point_str(self):
        output = ""
        output += str(self.__mount_point.get_x())
        output += " "
        output += str(self.__mount_point.get_y())
        return output

    def add_move(self, move):
        self.__move_list += str(" " + move)

    def set_task_to_completed(self, task):
        self.__completed_tasks.append(task)
        self.__tasks.remove(task)
    
    def print_robot_tasks_for_output(self):
        #information to be printed 
        #Line 2  mount point, number of tasks completed, number of commands
        #Line 3  task index
        #Line 4  move list
        output = ""
        output = output + str(self.get_mount_point_str()) + " "
        output = output + str(len(self.__completed_tasks)) + " "
        output = output + str(len(self.__move_list)) + " "
        output = output + "\n"
        for task in self.__completed_tasks:
            output = output + str(task.get_task_number()) + " "
        output = output + "\n"
        output = output + self.__move_list
        return output

        
    

#read the input file 
input_file = open("a_example.txt")

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
    t = Task(task, temp_list[0], temp_list[1])
    temp = input_file.readline() 
    temp_list = temp.split()
    for task_points in range(int(t.get_num_of_points())):
        assembly_point = Point(temp_list[task_points*2], temp_list[task_points*2 + 1])
        t.set_assembly_point_list(assembly_point)
    task_list.append(t)
  
#close the file and print the number of pizzas parsed
input_file.close()
print("parse successful.")


##code testsing can be commented 

r1_task_list = []
r2_task_list = []

r1_task_list.append(task_list[0])
r2_task_list.append(task_list[2])

r1 = Robot(mount_point_list[0], r1_task_list)
r1.add_move("U")
r1.add_move("W")
r2 = Robot(mount_point_list[1], r2_task_list)
r2.add_move("R")

robot_list = []
robot_list.append(r1)
robot_list.append(r2)

r1.set_task_to_completed(task_list[0])
r2.set_task_to_completed(task_list[2])

#output 
print(len(robot_list))
for robot in robot_list:
    print(robot.print_robot_tasks_for_output())
