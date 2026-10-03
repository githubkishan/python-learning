"""
practice/recursion_basics.py

Recursion: when a function calls ITSELF to solve a smaller version
of the same problem, until it reaches a simple "base case" it can
answer directly. Covers base cases, factorial, Fibonacci, summing
a list, and recursively walking nested data.

Run this file with:  python practice/recursion_basics.py
"""

print("=" * 60)
print("PART 1: THE SIMPLEST RECURSIVE FUNCTION")
print("=" * 60)

# Every recursive function needs two things:
#   1. A "base case" - the simple situation where it stops.
#   2. A "recursive case" - where it calls itself with a smaller problem.
def count_down(n):
    if n <= 0:              # base case: stop here
        print("Done!")
        return
    print(n)
    count_down(n - 1)       # recursive case: call itself with a smaller n

count_down(5)


print()
print("=" * 60)
print("PART 2: FACTORIAL (A CLASSIC RECURSION EXAMPLE)")
print("=" * 60)

# factorial(n) = n * (n-1) * (n-2) * ... * 1
# factorial(5) = 5 * factorial(4) = 5 * 4 * factorial(3) = ...
def factorial(n):
    if n <= 1:               # base case: factorial(0) and factorial(1) are both 1
        return 1
    return n * factorial(n - 1)   # recursive case

print("factorial(5):", factorial(5))
print("factorial(1):", factorial(1))


print()
print("=" * 60)
print("PART 3: FIBONACCI SEQUENCE")
print("=" * 60)

# Each Fibonacci number is the sum of the two before it: 0, 1, 1, 2, 3, 5, 8...
def fibonacci(n):
    if n <= 1:                # base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)   # recursive case

print("First 10 Fibonacci numbers:")
for i in range(10):
    print(fibonacci(i), end=" ")
print()


print()
print("=" * 60)
print("PART 4: SUMMING A LIST RECURSIVELY")
print("=" * 60)

# You don't need a loop to add up a list - recursion works too:
# sum of the list = first item + sum of everything else
def recursive_sum(numbers):
    if not numbers:            # base case: an empty list sums to 0
        return 0
    return numbers[0] + recursive_sum(numbers[1:])

verse_counts = [47, 72, 43, 20]
print("Recursive sum:", recursive_sum(verse_counts))


print()
print("=" * 60)
print("PART 5: RECURSION ON NESTED DATA")
print("=" * 60)

# Recursion really shines on data that can contain MORE of itself,
# like a list that might have other lists inside it.
def count_all_items(data):
    """Count every number, no matter how deeply nested."""
    total = 0
    for item in data:
        if isinstance(item, list):
            total += count_all_items(item)   # recurse into the nested list
        else:
            total += 1
    return total

nested_chapters = [1, 2, [3, 4, [5, 6]], 7, [8]]
print("Total items, including nested ones:", count_all_items(nested_chapters))


print()
print("=" * 60)
print("PART 6: PRACTICE EXERCISES WITH SOLUTIONS")
print("=" * 60)

# --- Exercise 1 ---
# Task: Write a recursive function that counts down AND up,
# printing numbers from 1 to n.
print("\nExercise 1: count up recursively")
def count_up(current, total):
    if current > total:        # base case
        return
    print(current, end=" ")
    count_up(current + 1, total)   # recursive case

count_up(1, 5)
print()

# --- Exercise 2 ---
# Task: Write a recursive function that reverses a string.
print("\nExercise 2: reverse a string recursively")
def reverse_string(text):
    if len(text) <= 1:          # base case: a single letter is its own reverse
        return text
    return reverse_string(text[1:]) + text[0]

print(reverse_string("Krishna"))

# --- Exercise 3 ---
# Task: Write a recursive function that finds the largest number
# in a list.
print("\nExercise 3: find the max value recursively")
def recursive_max(numbers):
    if len(numbers) == 1:       # base case: one item is the max of itself
        return numbers[0]
    rest_max = recursive_max(numbers[1:])
    return numbers[0] if numbers[0] > rest_max else rest_max

print("Max of [47, 72, 43, 20]:", recursive_max([47, 72, 43, 20]))

# --- Exercise 4 ---
# Task: Write a recursive function that checks if a word is a
# palindrome (reads the same forwards and backwards).
print("\nExercise 4: check for a palindrome recursively")
def is_palindrome(word):
    if len(word) <= 1:          # base case: 0 or 1 letters is always a palindrome
        return True
    if word[0] != word[-1]:     # first and last letters must match
        return False
    return is_palindrome(word[1:-1])   # check the middle part

print("'gita' is a palindrome:", is_palindrome("gita"))
print("'mom' is a palindrome:", is_palindrome("mom"))


print()
print("=" * 60)
print("PART 7: REAL WORLD EXAMPLE - COUNTING VERSES ACROSS CHAPTERS")
print("=" * 60)

# A realistic use of recursion: adding up verse counts from a list
# of chapters that's structured as "groups of groups".
chapter_groups = [
    [47, 72, 43],         # chapters 1-3
    [62, 29, 47],         # chapters 4-6
    [30, 28, 34],         # chapters 7-9
]

def total_verses(groups):
    """Recursively add up every verse count, no matter how the
    chapters are grouped."""
    total = 0
    for item in groups:
        if isinstance(item, list):
            total += total_verses(item)   # recurse into the sub-group
        else:
            total += item
    return total

print("Total verses across all groups:", total_verses(chapter_groups))

# Recursion also helps when printing a nested outline of chapters,
# where each "part" can contain either chapters or more parts.
gita_outline = {
    "name": "Bhagavad Gita",
    "parts": [
        {"name": "Arjuna's Dilemma", "parts": [
            {"name": "Chapter 1: Arjuna Vishada Yoga", "parts": []},
        ]},
        {"name": "Path of Action", "parts": [
            {"name": "Chapter 2: Sankhya Yoga", "parts": []},
            {"name": "Chapter 3: Karma Yoga", "parts": []},
        ]},
    ],
}

def print_outline(node, depth=0):
    print("  " * depth + node["name"])
    for part in node["parts"]:
        print_outline(part, depth + 1)   # recurse one level deeper

print("\nGita outline:")
print_outline(gita_outline)
