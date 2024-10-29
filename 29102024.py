Define a function called greet that takes a name as an argument and prints a greeting message like: "Hello, [name]!"


def greet(name):
 print(f"Hello, {name}!")

greet("Alice")


Write a function add_numbers that takes two numbers as arguments and returns their sum. Test the function by passing different numbers.


def add_numbers(num1, num2):
    return num1 + num2

# Test the function with different numbers
result1 = add_numbers(5, 3)
result2 = add_numbers(10, 15)
result3 = add_numbers(-1, 1)

print(result1)  
print(result2)  
print(result3)  


Create a function is_even that takes a number as an argument and returns True if the number is even, and False otherwise.


def is_even(number):
    return number % 2 == 0

print(is_even(4))  
print(is_even(7))  

Define a function find_max that takes three numbers as input and returns the largest of the three. Test the function with various sets of numbers.

def find_max(a, b, c):
    return max(a, b, c)

print(find_max(3, 7, 5))      
print(find_max(-10, 20, 15))  
print(find_max(0, -5, -2))

Write a function count_vowels that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("hello"))       
print(count_vowels("Beautiful"))   
print(count_vowels("Python"))  


Create a function is_prime that takes a number as input and returns True if the number is prime, and False otherwise.

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


print(is_prime(11))  
print(is_prime(15))  
print(is_prime(2)) 

Write a function find_common_elements that takes two lists as input and returns a list of elements that are present in both lists.

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

print(find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  
print(find_common_elements(['a', 'b', 'c'], ['c', 'd', 'e'])) 
print(find_common_elements([1, 2], [3, 4]))  


Write a function reverse_string that takes a string as input and returns the string reversed.


def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))    
print(reverse_string("Python"))  
print(reverse_string("12345"))    
