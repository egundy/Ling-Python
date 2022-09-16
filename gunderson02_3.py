'''Write a Python program to find and print common items from the two lists: [“ling”, “anth”, 
“math”, “lang”, “phil”, “engl”, “writ”, “cogsci”] and [“ling”, “stats”, “bio”, “cs” “ai”, “math”, 
“cogsci”]. Submit your script. '''


#initialize and assign lists
list_1 = ["ling", "anth", "math", "lang", "phil", "engl", "writ", "cogsci"]
list_2 = ["ling", "stats", "bio", "cs", "ai", "math", "cogsci"]

#check for common elements
list_3 = set(list_1) & set(list_2)

print(list(list_3)) #print result of function