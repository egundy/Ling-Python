'''The following code is problematic under the assumption that what I want to print is [4, 3, 2, 1]. 
What is the problem? How would you fix it? 
>>> my_list = [1, 2, 3, 4]
>>> my_list_copy = my_list.reverse( )
>>> print(my_list_copy)'''

#The code presented above will print 'None' instead of the reversed list
#This is because the variable 'my_list_copy' is reversing the list IN PLACE
#To return the desired output reversed() should be used


my_list = [1,2,3,4] #initialize and assign new list
my_list_copy = reversed(my_list) #reverse list,initialize, and assign new variable
print(list(my_list_copy)) #print the reversed list as a list

'''The code displayed reverses the list and assigns it to a new variable; 
    however, if .reverse() was to be used a new variable is redundant.
    Code that follows shows how to do that'''

# my_list.reverse()
# print(my_list)