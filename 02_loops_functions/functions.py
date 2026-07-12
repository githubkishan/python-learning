"""
02_loops_functions/functions.py

Functions let you package up code into a reusable, named block.
Covers def, parameters, default arguments, *args/**kwargs,
return values, docstrings, and lambda functions.

Run this file with:  python 02_loops_functions/functions.py
"""

print("=" * 60)
print("PART 1: DEFINING AND CALLING A FUNCTION")
print("=" * 60)

# "def" creates a function. Code inside it only runs when you CALL it.
def greet():
    print("Hare Krishna! Welcome to your Python journey.")

greet()   # calling the function runs the code inside it


print()
print("=" * 60)
print("PART 2: PARAMETERS - PASSING DATA IN")
print("=" * 60)

# A parameter is a variable that receives a value when the function is called.
def greet_person(name):
    print(f"Hare Krishna, {name}!")

greet_person("Arjuna")
greet_person("Kishan")

# You can have multiple parameters
def describe_chapter(number, name, verses):
    print(f"Chapter {number}: {name} has {verses} verses")

describe_chapter(2, "Sankhya Yoga", 72)


print()
print("=" * 60)
print("PART 3: DEFAULT ARGUMENTS")
print("=" * 60)

# A default argument is used automatically if the caller doesn't provide one
def greet_with_title(name, title="Devotee"):
    print(f"Greetings, {title} {name}")

greet_with_title("Kishan")                # uses the default title
greet_with_title("Arjuna", title="Warrior")  # overrides the default


print()
print("=" * 60)
print("PART 4: RETURN VALUES")
print("=" * 60)

# "return" sends a value back to whoever called the function,
# so you can store it or use it elsewhere in your code.
def add_verses(chapter_verses):
    total = sum(chapter_verses)
    return total

result = add_verses([47, 72, 43])
print("Total verses:", result)

# A function can return more than one value using a comma
def get_min_max(numbers):
    return min(numbers), max(numbers)

smallest, largest = get_min_max([47, 20, 5, 72, 11])
print(f"Smallest: {smallest}, Largest: {largest}")


print()
print("=" * 60)
print("PART 5: DOCSTRINGS - DOCUMENTING A FUNCTION")
print("=" * 60)

# A docstring is a short description placed right under "def",
# written inside triple quotes. It explains what the function does.
def calculate_average(numbers):
    """Return the average (mean) of a list of numbers."""
    return sum(numbers) / len(numbers)

print(calculate_average([47, 72, 43]))
print("Docstring:", calculate_average.__doc__)   # you can even read it back!


print()
print("=" * 60)
print("PART 6: *ARGS AND **KWARGS")
print("=" * 60)

# *args -> lets a function accept ANY number of positional arguments,
# collected into a tuple.
def total_verses(*args):
    return sum(args)

print("total_verses(47, 72, 43):", total_verses(47, 72, 43))
print("total_verses(20, 5):", total_verses(20, 5))

# **kwargs -> lets a function accept ANY number of named (keyword)
# arguments, collected into a dictionary.
def describe_student(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("describe_student(...):")
describe_student(name="Kishan", age=21, course="Python")


print()
print("=" * 60)
print("PART 7: LAMBDA FUNCTIONS (SHORT, ANONYMOUS FUNCTIONS)")
print("=" * 60)

# A lambda is a tiny, one-line, unnamed function.
# Pattern: lambda parameters: expression
square = lambda n: n ** 2
print("square(5):", square(5))

# Lambdas are often used inside functions like sorted() or max()
chapters = [
    {"name": "Karma Yoga", "verses": 43},
    {"name": "Jnana Yoga", "verses": 72},
]
sorted_by_verses = sorted(chapters, key=lambda c: c["verses"])
print("Sorted by verse count:", sorted_by_verses)


print()
print("=" * 60)
print("PART 8: VARIABLE SCOPE (LOCAL VS GLOBAL)")
print("=" * 60)

# A variable created INSIDE a function is "local" - it only exists there.
message = "global message"   # this is a "global" variable

def show_scope():
    message = "local message"   # this only exists inside this function
    print("Inside function:", message)

show_scope()
print("Outside function:", message)   # the global variable is unaffected


print()
print("=" * 60)
print("PART 9: PRACTICE EXERCISES WITH SOLUTIONS")
print("=" * 60)

# --- Exercise 1 ---
# Task: Write a function that takes a name and returns a greeting string
# (instead of printing it directly).
print("\nExercise 1: return a greeting")
def make_greeting(name):
    return f"Namaste, {name}!"

print(make_greeting("Kishan"))

# --- Exercise 2 ---
# Task: Write a function with a default parameter for the number of
# verses per day, and calculate how many days it takes to read a chapter.
print("\nExercise 2: default argument for a reading plan")
def days_to_finish(total_verses, verses_per_day=10):
    # -(-a // b) is a trick for "round up" division without importing math
    return -(-total_verses // verses_per_day)

print("Days needed for 47 verses:", days_to_finish(47))
print("Days needed for 47 verses at 5/day:", days_to_finish(47, verses_per_day=5))

# --- Exercise 3 ---
# Task: Write a function using *args that returns the longest word.
print("\nExercise 3: *args to find the longest word")
def longest_word(*words):
    return max(words, key=len)

print(longest_word("duty", "devotion", "self-realization"))

# --- Exercise 4 ---
# Task: Use a lambda with filter() to keep only chapters with
# more than 40 verses.
print("\nExercise 4: lambda with filter()")
chapter_verses = [47, 20, 5, 72, 11]
long_chapters = list(filter(lambda v: v > 40, chapter_verses))
print("Chapters with more than 40 verses:", long_chapters)


print()
print("=" * 60)
print("PART 10: REAL WORLD EXAMPLE - BHAGAVAD GITA STUDY TOOLKIT")
print("=" * 60)

# A small toolkit of functions to work with Gita data - this is how
# real programs are built: small, reusable functions doing one job each.

gita_shlokas = [
    {"chapter": 2, "verse": 47, "meaning": "Focus on your actions, not the results."},
    {"chapter": 2, "verse": 20, "meaning": "The soul is never born, and it never dies."},
    {"chapter": 6, "verse": 5, "meaning": "Lift yourself up by your own efforts."},
]

def find_shloka(shlokas, chapter, verse):
    """Search a list of shlokas and return the one matching chapter+verse."""
    for shloka in shlokas:
        if shloka["chapter"] == chapter and shloka["verse"] == verse:
            return shloka
    return None   # explicitly return None if nothing was found

def summarize(shlokas):
    """Print a one-line summary for every shloka in the list."""
    for shloka in shlokas:
        print(f"- {shloka['chapter']}.{shloka['verse']}: {shloka['meaning']}")

def count_by_chapter(shlokas, chapter):
    """Count how many shlokas we have stored for a given chapter."""
    matching = [s for s in shlokas if s["chapter"] == chapter]
    return len(matching)

# Use the toolkit
print("Full summary:")
summarize(gita_shlokas)

found = find_shloka(gita_shlokas, chapter=2, verse=47)
print(f"\nFound shloka 2.47: {found['meaning']}")

not_found = find_shloka(gita_shlokas, chapter=18, verse=66)
print("Searching for 18.66:", not_found)

print(f"\nShlokas stored for Chapter 2: {count_by_chapter(gita_shlokas, 2)}")
