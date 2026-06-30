# Iterate Through a Tuple and Print Types
# •	Task: Create a tuple with at least 5 different types of elements (int, float, string, bool, and complex).
# •	Use a for loop to iterate over the tuple and print each element along with its data type.
data_bag = (42, 3.14, "hello", True, 2+3j)
for item in data_bag:
    print(f"Value: {item} | Type: {type(item)}")





# Print All Items from a List with a Custom Message
# •	Task: Create a list of 4 different city names.
# •	Use a for loop to print each city name followed by the phrase "is a great place".
cities = ["Kathmandu", "Tokyo", "Berlin", "New York"]
for city in cities:
    print(f"{city} is a great place")




# Print Each Character of a String with Its Index
# •	Task: Ask the user to enter a word.
# •	Use a for loop and enumerate() to print each character of the string along with its index.
word = input("Enter a word: ")
for idx, char in enumerate(word):
    print(f"Index {idx}: {char}")






# Sum of Elements in a List
# •	Task: Create a list of integers.
# •	Use a for loop to calculate the sum of all the elements and print the total.
nums = [10, 20, 35, 5, 50]
total = 0
for n in nums:
    total += n
print(f"The sum is: {total}")






# Count Booleans in a Tuple
# •	Task: Create a tuple containing different data types, including multiple True and False values.
# •	Use a for loop to count how many True values are present and print the count.
mixed_data = (1, True, "off", False, 0.5, True, False, True)
true_count = 0
for item in mixed_data:
    if isinstance(item, bool) and item == True:
        true_count += 1
print(f"Found {true_count} True values.")






# Check and Print Data Types from a List
# •	Task: Create a list with at least 6 elements of different types (int, float, str, bool, etc.).
# •	Use a for loop to iterate through the list and print the data type of each element.
# A grab bag of different types
stuff = [100, 9.9, "code", False, [1, 2], {"key": "val"}]
for item in stuff:
    print(f"Item '{item}' is of type {type(item).__name__}")









# Check for Vowels in a String
# •	Task: Ask the user for a word.
# •	Use a for loop to check each character and print a message if it’s a vowel (a, e, i, o, u).
user_str = input("Enter a word: ").lower()
vowels = "aeiou"
for char in user_str:
    if char in vowels:
        print(f"'{char}' is a vowel!")






# Print Square of Numbers from a Tuple
# •	Task: Create a tuple of numbers from 1 to 5.
# •	Use a for loop to iterate through the tuple and print the square of each number.
nums = (1, 2, 3, 4, 5)
for n in nums:
    print(f"{n} squared is {n**2}")





# Print Elements of a List in Uppercase
# •	Task: Create a list of 5 small letter containing words.
# •	Use a for loop to iterate over the list and print each word in lowercase.
words = ["apple", "banana", "cherry", "date", "elderberry"]
for w in words:
    print(w.upper())





# Count Numbers Greater Than 10 in a List
# •	Task: Create a list of integers.
# •	Use a for loop to count how many numbers in the list are greater than 10.
# •	Print the final count.
vals = [2, 15, 8, 22, 10, 5, 30]
count = 0
for v in vals:
    if v > 10:
        count += 1
print(f"Count of numbers > 10: {count}")