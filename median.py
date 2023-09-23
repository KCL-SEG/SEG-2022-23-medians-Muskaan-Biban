"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [int(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
    
numbers.sort()
    
if len(numbers) % 2 != 0:
    print(numbers[len(numbers) // 2])
else:
    first = numbers[((len(numbers) // 2) - 1)]
    second = numbers[len(numbers) // 2]
    print((first + second) / 2)
