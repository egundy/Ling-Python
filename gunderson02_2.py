'''Write a Python program to find and print the second largest number in the list [2, 37, 10, 66, 23, 
1, 178, 19, 87]. Submit your script. '''

# To find the second largest number the list should be sorted
from random import randint


my_list = [2, 37, 10, 66, 23, 1, 178, 19, 87] #initializes and assigns list
my_list.sort() #sorts list smallest to largest
print(my_list)
print(my_list[-2]) #prints the second to last element in the list

#fun randint version
flag = 0
rand_list = []
while flag !=8:
    rand_list.append(randint(0,1000))
    flag += 1

rand_list.sort()
print(rand_list)
print(rand_list[-2])