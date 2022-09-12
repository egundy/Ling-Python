'''Write a Python program to find and print the second largest number in the list [2, 37, 10, 66, 23, 
1, 178, 19, 87]. Submit your script. '''

# To find the second largest number the list should be sorted
my_list = [2, 37, 10, 66, 23, 1, 178, 19, 87] #initializes and assigns list
my_list.sort() #sorts list smallest to largest
print(my_list[len(my_list)-2]) #prints the second to last element in the list