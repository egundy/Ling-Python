'''Write a Python program to find and print common items from the two lists: [“ling”, “anth”, 
“math”, “lang”, “phil”, “engl”, “writ”, “cogsci”] and [“ling”, “stats”, “bio”, “cs” “ai”, “math”, 
“cogsci”]. Submit your script. '''


#initialize and assign lists
list_1 = ["ling", "anth", "math", "lang", "phil", "engl", "writ", "cogsci"]
list_2 = ["ling", "stats", "bio", "cs", "ai", "math", "cogsci"]

#check for common elements
def common_elem(a,b):   #create function for finding common elements
    result = [i for i in a if i in b] #for loop to iterate through elements in each list and 
    return result
print(common_elem(list_1,list_2)) #print result of function