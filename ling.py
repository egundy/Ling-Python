#initialize and assign lists
list_a = [1,2,3,4,5,6]
list_b = [3,4,5,6,7,8]

result = set(list_a) & set(list_b) #find the common elements in the two lists
'''Optional solution in the comment below'''
# result = set(list_a) -(set(list_a) - set(list_b)) #find the common elements in the two lists below
print(list(result))