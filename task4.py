# Even or Odd Checker
# •	Task: Write a program that prompts the user for an integer.
# o	Use if/else to check whether the number is even or odd.
# o	Print "Even" or "Odd" accordingly.

num = int(input("Enter an integer: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")





# Positive, Negative, or Zero
# •	Task: Write a program that prompts the user for a number.
# o	Use if/elif/else to determine if the number is positive, negative, or zero.
# o	Print a message such as "The number is positive.".
val = float(input("Enter a number: "))
if val > 0:
    print("The number is positive.")
elif val < 0:
    print("The number is negative.")
else:
    print("The number is zero.")






# Grade Categorizer
# •	Task: Prompt the user for a number between 0 and 100 (the score).
# o	Use if/elif/else to categorize the score:
# 	90–100: "Grade A"
# 	80–89: "Grade B"
# 	70–79: "Grade C"
# 	< 70: "Fail"
score = float(input("Enter your score (0-100): "))
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Fail")









# Multiples of 3 and 5
# •	Task: Prompt the user for a single integer n.
# o	Use a for loop to iterate from 1 up to n (inclusive).
# o	For each value i, print:
# 	"Multiple of both" if i is divisible by 3 and 5.
# 	"Multiple of 3" if i is divisible by 3 but not 5.
# 	"Multiple of 5" if i is divisible by 5 but not 3.
# 	The number i itself otherwise.
n = int(input("Enter an integer n: "))

for i in range(1, n + 1):
    # Order matters: check the 'both' condition first so it doesn't get missed
    if i % 3 == 0 and i % 5 == 0:
        print("Multiple of both")
    elif i % 3 == 0:
        print("Multiple of 3")
    elif i % 5 == 0:
        print("Multiple of 5")
    else:
        print(i)








# Simple Password Check
# •	Task: Prompt the user for a password (e.g., "secret").
# o	Use if to check if the user’s input matches the correct password.
# o	If correct, print "Access granted", otherwise print "Access denied".
# Hardcoded secret for now; maybe move to an env variable later?
secret = "secret"
user_input = input("Enter password: ")

if user_input == secret:
    print("Access granted")
else:
    print("Access denied")







# Count Vowels in a String
# •	Task: Ask the user for a string.
# o	Use a for loop to iterate over each character.
# o	Use if conditions to check if it’s a vowel ("a", "e", "i", "o", "u").
# o	Count the total number of vowels and print the result.
text = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f"Total number of vowels: {count}")







# Smallest of Three Numbers
# •	Task: Prompt the user for three different numbers.
# o	Use if/elif/else to find and print which one is smallest
n1 = float(input("First number: "))
n2 = float(input("Second number: "))
n3 = float(input("Third number: "))
if n1 <= n2 and n1 <= n3:
    smallest = n1
elif n2 <= n1 and n2 <= n3:
    smallest = n2
else:
    smallest = n3
print(f"The smallest number is {smallest}")






# Simple Menu Selection
# •	Task: Prompt the user to choose an option (e.g., 1 for "Start", 2 for "Settings", 3 for "Exit").
# o	Use if/elif/else to print a response based on which option is chosen.
# o	Example:
# 	If user enters 1: print "Game starting..."
# 	If user enters 2: print "Opening settings..."
# 	If user enters 3 or any other: print "Exiting..."
print("1: Start\n2: Settings\n3: Exit")
choice = input("Select an option: ")
if choice == "1":
    print("Game starting...")
elif choice == "2":
    print("Opening settings...")
else:
    print("Exiting...")
