"""
03_numpy/numpy_basics.py

NumPy is a library for fast, powerful work with arrays of numbers.
It's the foundation of most data science and machine learning in Python.

Before running this file, install NumPy:
    pip install numpy

Run this file with:  python 03_numpy/numpy_basics.py
"""

import numpy as np   # "np" is the standard nickname everyone uses for numpy

print("=" * 60)
print("PART 1: CREATING ARRAYS")
print("=" * 60)

# A NumPy array is like a list, but built for fast math on numbers.
verse_counts = np.array([47, 72, 43, 47, 19])
print("Array:", verse_counts)
print("Type:", type(verse_counts))

# np.zeros(n) / np.ones(n) -> quickly build arrays filled with 0s or 1s
print("np.zeros(5):", np.zeros(5))
print("np.ones(3):", np.ones(3))

# np.arange(start, stop, step) -> like Python's range(), but returns an array
chapters = np.arange(1, 19)   # chapters 1 to 18
print("Chapters 1-18:", chapters)

# np.linspace(start, stop, num) -> "num" evenly spaced numbers between start/stop
progress_points = np.linspace(0, 100, 5)
print("5 evenly spaced progress points:", progress_points)


print()
print("=" * 60)
print("PART 2: ARRAY SHAPE AND INDEXING")
print("=" * 60)

# .shape tells you the array's dimensions (rows, columns)
print("Shape of verse_counts:", verse_counts.shape)

# Indexing and slicing work just like with regular Python lists
print("First value:", verse_counts[0])
print("Last value:", verse_counts[-1])
print("First 3 values:", verse_counts[:3])

# A 2D array (matrix) - think of it as a grid of rows and columns
verse_matrix = np.array([
    [1, 47],   # [chapter, verses]
    [2, 72],
    [3, 43],
])
print("\n2D array:\n", verse_matrix)
print("Shape:", verse_matrix.shape)          # (3 rows, 2 columns)
print("Row 0:", verse_matrix[0])
print("Element at row 1, column 1:", verse_matrix[1, 1])


print()
print("=" * 60)
print("PART 3: ARRAY MATH (VECTORIZED OPERATIONS)")
print("=" * 60)

# This is the superpower of NumPy: apply an operation to EVERY item
# at once, without writing a loop.
numbers = np.array([1, 2, 3, 4, 5])
print("Original:", numbers)
print("+ 10:", numbers + 10)
print("* 2:", numbers * 2)
print("squared:", numbers ** 2)

# You can also do math between two arrays of the same shape
verses_last_year = np.array([40, 70, 45])
verses_this_year = np.array([47, 72, 43])
difference = verses_this_year - verses_last_year
print("Difference:", difference)


print()
print("=" * 60)
print("PART 4: USEFUL STATISTICS FUNCTIONS")
print("=" * 60)

verse_counts = np.array([47, 72, 43, 47, 19, 20, 24])

print("Sum:", np.sum(verse_counts))
print("Mean (average):", np.mean(verse_counts))
print("Max:", np.max(verse_counts))
print("Min:", np.min(verse_counts))
print("Standard deviation:", round(np.std(verse_counts), 2))
print("Sorted:", np.sort(verse_counts))


print()
print("=" * 60)
print("PART 5: FILTERING WITH BOOLEAN CONDITIONS")
print("=" * 60)

# Comparing an array to a number gives back an array of True/False values
verse_counts = np.array([47, 72, 43, 47, 19, 20, 24])
is_long_chapter = verse_counts > 40
print("Which chapters are 'long' (>40 verses)?", is_long_chapter)

# You can use that True/False array to filter the original array directly
long_chapters = verse_counts[is_long_chapter]
print("Long chapters only:", long_chapters)

# Or do it in one line
short_chapters = verse_counts[verse_counts <= 20]
print("Short chapters only:", short_chapters)


print()
print("=" * 60)
print("PART 6: PRACTICE EXERCISES WITH SOLUTIONS")
print("=" * 60)

# --- Exercise 1 ---
# Task: Create an array of the numbers 1 to 18 (chapters) and print
# their total sum.
print("\nExercise 1: sum an array of chapter numbers")
chapters = np.arange(1, 19)
print("Sum of chapters 1-18:", np.sum(chapters))

# --- Exercise 2 ---
# Task: Given an array of verse counts, calculate the average
# rounded to 1 decimal place.
print("\nExercise 2: average verse count")
verse_counts = np.array([47, 72, 43, 47, 19])
average = round(np.mean(verse_counts), 1)
print("Average verses per chapter:", average)

# --- Exercise 3 ---
# Task: Double every value in an array without using a loop.
print("\nExercise 3: double every value")
numbers = np.array([2, 4, 6, 8])
doubled = numbers * 2
print("Doubled:", doubled)

# --- Exercise 4 ---
# Task: Filter an array to find chapters with fewer than 25 verses.
print("\nExercise 4: filter short chapters")
verse_counts = np.array([47, 72, 43, 20, 19, 24])
short_chapters = verse_counts[verse_counts < 25]
print("Chapters with fewer than 25 verses:", short_chapters)


print()
print("=" * 60)
print("PART 7: REAL WORLD EXAMPLE - BHAGAVAD GITA VERSE STATISTICS")
print("=" * 60)

# Verse counts for the first 6 chapters of the Bhagavad Gita
chapter_numbers = np.arange(1, 7)
verse_counts = np.array([47, 72, 43, 42, 29, 47])

print("Chapter numbers:", chapter_numbers)
print("Verse counts   :", verse_counts)

# Combine both arrays into a readable report using zip() (regular Python,
# works fine alongside NumPy arrays)
print("\nChapter report:")
for chapter, verses in zip(chapter_numbers, verse_counts):
    print(f"  Chapter {chapter}: {verses} verses")

print(f"\nTotal verses in first 6 chapters: {np.sum(verse_counts)}")
print(f"Average verses per chapter: {np.mean(verse_counts):.2f}")
print(f"Longest chapter has {np.max(verse_counts)} verses "
      f"(Chapter {chapter_numbers[np.argmax(verse_counts)]})")

# np.argmax() returns the INDEX of the largest value - useful for
# finding "which chapter", not just "what's the biggest number"
shortest_index = np.argmin(verse_counts)
print(f"Shortest chapter is Chapter {chapter_numbers[shortest_index]} "
      f"with {verse_counts[shortest_index]} verses")
