# movies = []
# mov1 = input("enter fav mov:")
# mov2 = input("enter fav mov:")
# mov3 = input("enter fav mov:")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(f"these are the fav mov: {movies}")



# value = [1, 2, 1]

# copied = value.copy()
# copied.reverse()

# if(copied == value):
#     print("palindrome")
# elif(copied != value):
#     print("not palindrome")
# else:
#     print("Exit")


#-------------------------------------------Dictionary & Set in python----------------------------------------------------------
# info = {
#     "key" : "value",
#     "name" : "bibek",
#     "learning" : "coding",
#     "age" : 20,
#     "is adult" : True,
#     "subject" : ["python","Mysql","numpie"],
#     "topics" : ("dict", "set")
# }

# print(info["topics"])

# #nested dictonary
# student = {
#     "name" : "bibek",
    
#     "subject" : {
#         "math" : 67,
#         "science" : 77,
#         "english" : 102,
#         "optmath" : 54
#     },
#     "rollno" : 2

# }
# print(student["subject"]["math"])

# print("bibek")



# bibek = {
#     "name" : "Bibek_Parajuli",
#     "age" : 20,
#     "p_address": "lamjung",
#     "t_address" : "ktm",
#     "subject" : {
#         "math" : 22,
#         "sci" : 21,
#         "eng" : 44,
#         }
# }






# bibek = {"city" : "balaju"}
# print(bibek)
#myDict.keys()      #returns all keys
#myDict.values()      #returns all values
#myDict.items()     #returns all (keys, val) pairs as tuple
#mydict.get("key")     #returns the key according to value
#mydict.update(newDict)  #inserts the specified items in the dictionary












#--------------------------set in python-------------------------------------
# Set is the collection of the unordered items.
# Each elements in the set must be unique & immutable.

mums = {1,2,3,4}
set2 = {1,2,2,2}

#repeted elements stored only once, so it restores to {1,2}

null_set = set()      #empty set syntax