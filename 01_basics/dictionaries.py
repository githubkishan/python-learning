"""
01_basics/dictionaries.py

Dictionaries: Python's key-value storage. Great for representing
real-world records like a person, a book, or a verse.

Run this file with:  python 01_basics/dictionaries.py
"""

print("=" * 60)
print("PART 1: CREATING AND ACCESSING DICTIONARIES")
print("=" * 60)

# A dictionary stores data as key: value pairs inside curly brackets { }.
# Think of a key like a label on a labeled box, and the value is what's inside.
shloka = {
    "chapter": 2,
    "verse": 47,
    "speaker": "Krishna",
}
print("Dictionary:", shloka)

# Access a value using its key inside square brackets
print("Chapter:", shloka["chapter"])

# .get(key) -> safer way to access a value; returns None (not an error)
# if the key doesn't exist
print("Speaker:", shloka.get("speaker"))
print("Missing key with get():", shloka.get("translator"))
print("Missing key with default:", shloka.get("translator", "Unknown"))


print()
print("=" * 60)
print("PART 2: ADDING, UPDATING, AND REMOVING")
print("=" * 60)

# Add a new key-value pair simply by assigning it
shloka["theme"] = "Duty without attachment"
print("After adding 'theme':", shloka)

# Update an existing value the same way
shloka["speaker"] = "Lord Krishna"
print("After updating 'speaker':", shloka)

# .update() -> merge multiple key-value pairs at once
shloka.update({"chapter": 2, "translator": "Eknath Easwaran"})
print("After update():", shloka)

# .pop(key) -> removes a key and returns its value
removed_value = shloka.pop("translator")
print("Removed value:", removed_value)
print("After pop():", shloka)


print()
print("=" * 60)
print("PART 3: LOOPING THROUGH A DICTIONARY")
print("=" * 60)

person = {"name": "Kishan", "age": 21, "city": "Delhi"}

# .keys() -> just the keys
print("Keys:", list(person.keys()))

# .values() -> just the values
print("Values:", list(person.values()))

# .items() -> key-value pairs together, useful for looping
print("Items:", list(person.items()))

print("\nLooping with .items():")
for key, value in person.items():
    print(f"  {key} -> {value}")


print()
print("=" * 60)
print("PART 4: NESTED DICTIONARIES")
print("=" * 60)

# A nested dictionary stores a dictionary INSIDE another dictionary.
# Perfect for representing structured records, like a student with grades.
student = {
    "name": "Kishan",
    "grades": {"python": 95, "math": 88},
}
print("Nested dictionary:", student)
print("Python grade:", student["grades"]["python"])


print()
print("=" * 60)
print("PART 5: DICTIONARY COMPREHENSIONS")
print("=" * 60)

# Just like list comprehensions, but for dictionaries.
# Pattern: {key_expr: value_expr for item in iterable}
numbers = [1, 2, 3, 4, 5]
squares_dict = {n: n ** 2 for n in numbers}
print("Number -> square:", squares_dict)


print()
print("=" * 60)
print("PART 6: PRACTICE EXERCISES WITH SOLUTIONS")
print("=" * 60)

# --- Exercise 1 ---
# Task: Create a dictionary about yourself with name, age, and hobby,
# then print a sentence describing you using an f-string.
print("\nExercise 1: describe yourself with a dictionary")
me = {"name": "Kishan", "age": 21, "hobby": "learning Python"}
print(f"{me['name']} is {me['age']} years old and enjoys {me['hobby']}.")

# --- Exercise 2 ---
# Task: Given a dictionary of item prices, calculate the total cost.
print("\nExercise 2: sum dictionary values")
cart = {"book": 300, "pen": 20, "notebook": 50}
total_cost = sum(cart.values())
print(f"Total cost: {total_cost}")

# --- Exercise 3 ---
# Task: Check if a key exists in a dictionary before accessing it.
print("\nExercise 3: safely check for a key")
settings = {"theme": "dark"}
if "language" in settings:
    print("Language:", settings["language"])
else:
    print("Language not set, defaulting to English")

# --- Exercise 4 ---
# Task: Use a dictionary comprehension to build a mapping of
# chapter number -> verse count, but only for chapters with > 40 verses.
print("\nExercise 4: filtered dictionary comprehension")
chapter_verses = {1: 47, 2: 72, 3: 43, 12: 20}
long_chapters = {ch: v for ch, v in chapter_verses.items() if v > 40}
print("Chapters with more than 40 verses:", long_chapters)


print()
print("=" * 60)
print("PART 7: REAL WORLD EXAMPLE - BHAGAVAD GITA VERSE LOOKUP")
print("=" * 60)

# A dictionary of dictionaries: a simple "database" of shlokas,
# keyed by "chapter.verse" so we can look any one up instantly.
gita_lookup = {
    "2.47": {
        "sanskrit": "Karmanye vadhikaraste Ma Phaleshu Kadachana",
        "meaning": "You have the right to perform your duty, "
                   "but never to the fruits of your actions.",
    },
    "2.20": {
        "sanskrit": "Na jayate mriyate va kadachin",
        "meaning": "The soul is never born, and it never dies.",
    },
    "6.5": {
        "sanskrit": "Uddhared atmanatmanam",
        "meaning": "Lift yourself up by your own efforts.",
    },
}

# Look up a specific verse instantly using its key
verse_key = "2.47"
verse = gita_lookup[verse_key]
print(f"Looking up {verse_key}:")
print(f"  Sanskrit: {verse['sanskrit']}")
print(f"  Meaning : {verse['meaning']}")

# Loop through the whole lookup table and print every verse
print("\nAll verses in the lookup table:")
for key, details in gita_lookup.items():
    print(f"- {key}: {details['meaning']}")

# Safely handle a verse that might not exist
missing_key = "18.66"
result = gita_lookup.get(missing_key, {"meaning": "Verse not found in our table"})
print(f"\nLooking up {missing_key}: {result['meaning']}")
