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
info = {
    "key" : "value",
    "name" : "bibek",
    "learning" : "coding",
    "age" : 20,
    "is adult" : True,
    "subject" : ["python","Mysql","numpie"],
    "topics" : ("dict", "set")
}

print(info["topics"])

#nested dictonary
student = {
    "name" : "bibek",
    
    "subject" : {
        "math" : 67,
        "science" : 77,
        "english" : 102,
        "optmath" : 54
    },
    "rollno" : 2

}
print(student["subject"]["math"])