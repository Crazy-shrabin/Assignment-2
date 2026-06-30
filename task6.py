# Print Numbers from 10 to 30
# •	Use a while loop to print numbers from 10 to 30.
i = 10
while i <= 30:
    print(i)
    i += 1




# Print Odd Numbers from 1 to 20
# •	Use a while loop to print all odd numbers from 1 to 20.
i = 1
while i <= 20:
    # Only print if the number isn't divisible by 2
    if i % 2 != 0:
        print(i)
    i += 1




# Print a Word 5 Times
# •	Use a while loop to print the word "Hello" five times.
count = 0
while count < 5:
    print("Hello")
    count += 1




# Countdown from 5
# •	Use a while loop to print numbers from 5 to 1.
n = 5
while n > 0:
    print(n)
    n -= 1





# Print All Multiples of 3 up to 30
# •	Use a while loop to print 3, 6, 9, ..., up to 30.
i = 3
while i <= 30:
    print(i)
    i += 3 





# Keep Asking for a Number Until It's Positive
# •	Keep asking the user to enter a number until they enter a positive number.
num = -1
while num <= 0:
    num = float(input("Please enter a positive number: "))
print(f"Thanks! You entered {num}.")




# Print Even Numbers Between 10 and 20
# •	Use a while loop to print even numbers from 10 to 20.
i = 10
while i <= 20:
    print(i)
    i += 2




# Guess the Secret Number using while loop
# •	Secret number = 7.
# •	Ask the user to guess the number until it's correct.
secret = 7
guess = 0
while guess != secret:
    guess = int(input("Guess the secret number: "))
    if guess != secret:
        print("Try again!")
print("You guessed it!")




# Function to Add Two Numbers
# •	Create a function add(a, b) that returns the sum.
def add(a, b):
    return a + b







# Function to Multiply Two Numbers
# •	Create a function multiply(x, y) that returns the product.
def multiply(x, y):
    return x * y



# Function to Check Even or Odd
# •	Create a function check_even(num) that prints "Even" or "Odd".
def check_even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")