"""
01_basics/variables.py

A beginner-friendly tour of Python variables and data types.
Every section has plain-English comments, runnable examples,
and practice exercises with solutions at the end.

Run this file with:  python 01_basics/variables.py
"""

print("=" * 60)
print("PART 1: ALL DATA TYPES WITH EXAMPLES")
print("=" * 60)

# A variable is just a "labeled box" that stores a value.
# Python figures out the data type automatically - you don't
# need to declare it like in some other languages.

# 1. Integer (int) -> whole numbers, no decimal point
age = 25
print("int example:", age, "| type:", type(age))

# 2. Float (float) -> numbers with a decimal point
height_in_meters = 5.9
print("float example:", height_in_meters, "| type:", type(height_in_meters))

# 3. String (str) -> text, written inside quotes
name = "Arjuna"
print("str example:", name, "| type:", type(name))

# 4. Boolean (bool) -> only two values: True or False
is_learning_python = True
print("bool example:", is_learning_python, "| type:", type(is_learning_python))

# 5. List -> an ordered collection that CAN be changed (mutable)
#    Written with square brackets [ ]
fruits = ["apple", "banana", "mango"]
print("list example:", fruits, "| type:", type(fruits))

# 6. Tuple -> an ordered collection that CANNOT be changed (immutable)
#    Written with round brackets ( )
coordinates = (10, 20)
print("tuple example:", coordinates, "| type:", type(coordinates))

# 7. Dictionary (dict) -> stores data as key-value pairs
#    Written with curly brackets { } like {key: value}
student = {"name": "Kishan", "age": 30, "course": "Python"}
print("dict example:", student, "| type:", type(student))

# 8. Set -> an unordered collection with NO duplicate values
#    Written with curly brackets { } but no key-value pairs
unique_numbers = {1, 2, 2, 3, 3, 3}
print("set example:", unique_numbers, "| type:", type(unique_numbers))

# 9. NoneType -> represents "no value" or "empty" on purpose
answer = None
print("NoneType example:", answer, "| type:", type(answer))

# 10. Complex numbers -> numbers with a real and imaginary part
#     Rarely used by beginners, but good to know it exists
complex_number = 3 + 4j
print("complex example:", complex_number, "| type:", type(complex_number))


print()
print("=" * 60)
print("PART 2: STRING METHODS (upper, lower, split, join, replace)")
print("=" * 60)

sentence = "Krishna teaches Arjuna in the Bhagavad Gita"

# .upper() -> converts ALL letters to uppercase
print("upper():", sentence.upper())

# .lower() -> converts all letters to lowercase
print("lower():", sentence.lower())

# .split() -> breaks a string into a list of words
#             by default it splits on spaces
words = sentence.split()
print("split():", words)

# .join() -> opposite of split, it glues a list of strings
#            together using a separator string
joined_with_dash = "-".join(words)
print("join():", joined_with_dash)

# .replace(old, new) -> swaps every occurrence of "old" with "new"
print("replace():", sentence.replace("Arjuna", "everyone"))


print()
print("=" * 60)
print("PART 3: F-STRINGS FORMATTING")
print("=" * 60)

# An f-string lets you put variables directly inside a string
# by writing f"..." and wrapping the variable in curly braces {}
warrior = "Arjuna"
guide = "Krishna"
chapter = 2

# Basic f-string
print(f"{guide} guides {warrior} in Chapter {chapter}.")

# You can also do quick math or calculations inside the braces
total_chapters = 18
completed_chapters = 2
print(f"Progress: {completed_chapters}/{total_chapters} chapters "
      f"({completed_chapters / total_chapters:.1%} done)")

# .2f formats a float to 2 decimal places
pi_value = 3.14159265
print(f"Pi rounded to 2 decimals: {pi_value:.2f}")


print()
print("=" * 60)
print("PART 4: PRACTICE EXERCISES WITH SOLUTIONS")
print("=" * 60)

# --- Exercise 1 ---
# Task: Create a variable holding your favorite number, then
# print its type using an f-string.
print("\nExercise 1: print a number and its type")
favorite_number = 7          # <- try changing this
print(f"My favorite number is {favorite_number}, "
      f"its type is {type(favorite_number)}")

# --- Exercise 2 ---
# Task: Take the sentence below, split it into words, and
# join it back together using "_" instead of spaces.
print("\nExercise 2: split and rejoin a sentence")
practice_sentence = "The Gita teaches duty without attachment"
split_words = practice_sentence.split()          # step 1: split
underscored = "_".join(split_words)              # step 2: join
print("Result:", underscored)

# --- Exercise 3 ---
# Task: Given a dictionary of a person's details, print a
# nicely formatted sentence using an f-string.
print("\nExercise 3: format a dictionary with an f-string")
person = {"name": "Kishan", "age": 21, "city": "Delhi"}
print(f"{person['name']} is {person['age']} years old "
      f"and lives in {person['city']}.")

# --- Exercise 4 ---
# Task: Replace a word in a string and convert the result
# to uppercase, all in one line.
print("\nExercise 4: chain string methods together")
quote = "peace comes from within"
result = quote.replace("peace", "strength").upper()
print("Result:", result)


print()
print("=" * 60)
print("PART 5: REAL WORLD EXAMPLES - BHAGAVAD GITA SHLOKAS")
print("=" * 60)

# Here we use variables and data types to organize real
# shlokas (verses) from the Bhagavad Gita. This shows how
# programming concepts apply to real, meaningful data.

# A dictionary storing a shloka and its details
shloka_2_47 = {
    "chapter": 2,
    "verse": 47,
    "sanskrit": "Karmanye vadhikaraste Ma Phaleshu Kadachana",
    "meaning": "You have the right to perform your duty, "
               "but never to the fruits of your actions.",
}

# f-string used to display the shloka nicely
print(f"Bhagavad Gita {shloka_2_47['chapter']}.{shloka_2_47['verse']}")
print(f"Sanskrit: {shloka_2_47['sanskrit']}")
print(f"Meaning : {shloka_2_47['meaning']}")

# A list of multiple shlokas, each stored as a dictionary
gita_shlokas = [
    {
        "chapter": 2, "verse": 47,
        "sanskrit": "Karmanye vadhikaraste Ma Phaleshu Kadachana",
        "meaning": "Focus on your actions, not on the results.",
    },
    {
        "chapter": 2, "verse": 20,
        "sanskrit": "Na jayate mriyate va kadachin",
        "meaning": "The soul is never born, and it never dies.",
    },
    {
        "chapter": 6, "verse": 5,
        "sanskrit": "Uddhared atmanatmanam",
        "meaning": "Lift yourself up by your own efforts; "
                   "do not degrade yourself.",
    },
]

# Loop through the list and print each shloka using f-strings
print("\nAll stored shlokas:")
for shloka in gita_shlokas:
    print(f"- Chapter {shloka['chapter']}, Verse {shloka['verse']}: "
          f"{shloka['meaning']}")

# Using string methods on shloka text: count words in a shloka
sanskrit_line = gita_shlokas[0]["sanskrit"]
word_count = len(sanskrit_line.split())
print(f"\nThe first shloka's Sanskrit line has {word_count} words.")

# Using .upper() to emphasize the core teaching
core_teaching = "focus on your duty, not the results"
print(f"\nCore teaching (emphasized): {core_teaching.upper()}")

# Building a summary sentence with an f-string using multiple variables
favorite_chapter = gita_shlokas[0]["chapter"]
favorite_meaning = gita_shlokas[0]["meaning"]
print(f"\nMy favorite teaching is from Chapter {favorite_chapter}: "
      f"\"{favorite_meaning}\"")
