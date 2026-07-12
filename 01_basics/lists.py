"""
01_basics/lists.py

Lists: Python's flexible, ordered, changeable collection.
Covers creation, indexing/slicing, common methods, list
comprehensions, and nested lists.

Run this file with:  python 01_basics/lists.py
"""

print("=" * 60)
print("PART 1: CREATING AND ACCESSING LISTS")
print("=" * 60)

# A list is an ordered collection written inside square brackets [ ].
# Lists can hold mixed data types, and they are MUTABLE (changeable).
chapters = ["Arjuna Vishada Yoga", "Sankhya Yoga", "Karma Yoga"]
print("List:", chapters)

# Access items by index (starts at 0)
print("First chapter:", chapters[0])
print("Last chapter:", chapters[-1])

# Slicing works just like with strings: list[start:stop]
print("First two chapters:", chapters[0:2])

# len() tells you how many items are in the list
print("Number of chapters:", len(chapters))


print()
print("=" * 60)
print("PART 2: CHANGING A LIST (MUTABILITY)")
print("=" * 60)

# Unlike strings, you CAN change a list item directly by index
chapters[0] = "Arjuna Vishada Yogam"   # fixed the spelling
print("After editing index 0:", chapters)

# .append(item) -> adds one item to the end of the list
chapters.append("Jnana Yoga")
print("After append():", chapters)

# .insert(position, item) -> adds an item at a specific position
chapters.insert(1, "Vishada Yoga")
print("After insert():", chapters)

# .remove(item) -> removes the FIRST matching item by value
chapters.remove("Vishada Yoga")
print("After remove():", chapters)

# .pop() -> removes and returns the LAST item (or a chosen index)
last_chapter = chapters.pop()
print("Popped item:", last_chapter)
print("After pop():", chapters)


print()
print("=" * 60)
print("PART 3: SORTING AND REVERSING")
print("=" * 60)

verse_counts = [47, 20, 5, 72, 11]

# .sort() -> sorts the list in place (changes the original list)
verse_counts.sort()
print("Sorted ascending:", verse_counts)

verse_counts.sort(reverse=True)
print("Sorted descending:", verse_counts)

# .reverse() -> flips the current order of the list
verse_counts.reverse()
print("Reversed:", verse_counts)

# sorted() -> like .sort(), but returns a NEW list and keeps the original
numbers = [5, 3, 8, 1]
new_sorted = sorted(numbers)
print("Original untouched:", numbers)
print("New sorted list:", new_sorted)


print()
print("=" * 60)
print("PART 4: LIST COMPREHENSIONS")
print("=" * 60)

# A list comprehension is a short way to build a new list from another one.
# Basic pattern: [expression for item in iterable if condition]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Example: square every number
squares = [n ** 2 for n in numbers]
print("Squares:", squares)

# Example: keep only even numbers
even_numbers = [n for n in numbers if n % 2 == 0]
print("Even numbers:", even_numbers)

# Example: uppercase every word in a list
words = ["duty", "devotion", "peace"]
upper_words = [w.upper() for w in words]
print("Uppercased:", upper_words)


print()
print("=" * 60)
print("PART 5: NESTED LISTS (LISTS INSIDE LISTS)")
print("=" * 60)

# A nested list is useful for grid-like or grouped data
chapter_groups = [
    ["Arjuna Vishada Yoga", "Sankhya Yoga"],   # Karma-focused chapters
    ["Bhakti Yoga", "Raja Vidya Yoga"],        # Devotion-focused chapters
]
print("Nested list:", chapter_groups)
print("First group:", chapter_groups[0])
print("First chapter of second group:", chapter_groups[1][0])


print()
print("=" * 60)
print("PART 6: PRACTICE EXERCISES WITH SOLUTIONS")
print("=" * 60)

# --- Exercise 1 ---
# Task: Create a list of your 3 favorite numbers, then print the sum.
print("\nExercise 1: sum a list of numbers")
favorite_numbers = [7, 21, 108]
print("Sum:", sum(favorite_numbers))

# --- Exercise 2 ---
# Task: Given a list of chapter names, add a new chapter at the end,
# then print the total count.
print("\nExercise 2: append and count")
gita_chapters = ["Karma Yoga", "Jnana Yoga"]
gita_chapters.append("Bhakti Yoga")
print("Chapters:", gita_chapters)
print("Total chapters:", len(gita_chapters))

# --- Exercise 3 ---
# Task: Use a list comprehension to find all verse counts greater than 40.
print("\nExercise 3: filter with a list comprehension")
verse_counts = [47, 20, 5, 72, 11, 55]
long_chapters = [v for v in verse_counts if v > 40]
print("Chapters with more than 40 verses:", long_chapters)

# --- Exercise 4 ---
# Task: Remove duplicate values from a list while keeping the result as a list.
print("\nExercise 4: remove duplicates")
raw_numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = list(set(raw_numbers))   # set() drops duplicates automatically
print("Unique numbers:", sorted(unique_numbers))


print()
print("=" * 60)
print("PART 7: REAL WORLD EXAMPLE - BHAGAVAD GITA CHAPTER TRACKER")
print("=" * 60)

# A list of dictionaries: a very common real-world pattern for storing
# multiple records (like rows in a spreadsheet or database table).
gita_chapters_data = [
    {"number": 1, "name": "Arjuna Vishada Yoga", "verses": 47},
    {"number": 2, "name": "Sankhya Yoga", "verses": 72},
    {"number": 3, "name": "Karma Yoga", "verses": 43},
    {"number": 6, "name": "Dhyana Yoga", "verses": 47},
]

# Loop through the list and print a formatted summary for each chapter
for chapter in gita_chapters_data:
    print(f"Chapter {chapter['number']}: {chapter['name']} "
          f"({chapter['verses']} verses)")

# Use a list comprehension to pull out just the chapter names
all_names = [chapter["name"] for chapter in gita_chapters_data]
print("\nAll chapter names:", all_names)

# Find the chapter with the most verses using max() with a "key" function
longest_chapter = max(gita_chapters_data, key=lambda c: c["verses"])
print(f"\nLongest chapter: {longest_chapter['name']} "
      f"with {longest_chapter['verses']} verses")

# Calculate the total number of verses read so far
total_verses = sum(chapter["verses"] for chapter in gita_chapters_data)
print(f"Total verses tracked: {total_verses}")
