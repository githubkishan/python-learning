"""
01_basics/strings.py

A deeper look at Python strings: indexing, slicing, immutability,
escape characters, and more string methods than variables.py covered.

Run this file with:  python 01_basics/strings.py
"""

print("=" * 60)
print("PART 1: WHAT IS A STRING?")
print("=" * 60)

# A string is just text, written inside single '...' or double "..." quotes.
# Both work the same way - pick one style and stay consistent.
greeting = "Hare Krishna"
another_way = 'Hare Krishna'
print(greeting == another_way)  # True, they hold the same text

# Triple quotes let a string span multiple lines
multiline_verse = """Karmanye vadhikaraste
Ma Phaleshu Kadachana"""
print(multiline_verse)


print()
print("=" * 60)
print("PART 2: INDEXING AND SLICING")
print("=" * 60)

# Every character in a string has a position, called an index.
# Indexing starts at 0, NOT 1.
word = "Krishna"
print("First letter:", word[0])     # 'K'
print("Last letter:", word[-1])     # 'a' (negative index counts from the end)

# Slicing takes out a chunk: word[start:stop]
# "stop" is NOT included in the result.
print("First 3 letters:", word[0:3])   # 'Kri'
print("Letters 2 to end:", word[2:])   # 'ishna'
print("Reversed word:", word[::-1])    # step of -1 reverses the string


print()
print("=" * 60)
print("PART 3: STRINGS ARE IMMUTABLE")
print("=" * 60)

# Immutable means "cannot be changed after creation".
# You CANNOT do word[0] = "P" - that would raise a TypeError.
# Instead, you build a NEW string.
original = "Arjuna"
changed = "P" + original[1:]   # replace first letter by slicing + concatenating
print("Original:", original)
print("New string:", changed)


print()
print("=" * 60)
print("PART 4: ESCAPE CHARACTERS")
print("=" * 60)

# Escape characters start with a backslash \ and mean "special instruction"
print("Line 1\nLine 2")          # \n = new line
print("Column1\tColumn2")        # \t = tab space
print("She said \"Peace\" softly")  # \" = a literal quote mark inside a string


print()
print("=" * 60)
print("PART 5: MORE STRING METHODS")
print("=" * 60)

line = "   The Gita has 700 verses   "

# .strip() -> removes extra whitespace from both ends
print(f"strip(): '{line.strip()}'")

# .find(sub) -> returns the index where a substring starts, or -1 if missing
print("find('Gita'):", line.find("Gita"))
print("find('Mahabharata'):", line.find("Mahabharata"))

# .count(sub) -> counts how many times a substring appears
print("count('e'):", line.count("e"))

# .startswith() / .endswith() -> check the beginning/end of a string
title = "Bhagavad Gita"
print("startswith('Bhagavad'):", title.startswith("Bhagavad"))
print("endswith('Gita'):", title.endswith("Gita"))

# .isdigit() -> True if the string contains only numbers
print("'700'.isdigit():", "700".isdigit())
print("'seven'.isdigit():", "seven".isdigit())

# .title() -> capitalizes the first letter of every word
print("title():", "the bhagavad gita".title())


print()
print("=" * 60)
print("PART 6: PRACTICE EXERCISES WITH SOLUTIONS")
print("=" * 60)

# --- Exercise 1 ---
# Task: Print the first 5 characters and the last 5 characters
# of the word "Mahabharata" using slicing.
print("\nExercise 1: slice the first and last 5 letters")
epic = "Mahabharata"
print("First 5:", epic[:5])
print("Last 5:", epic[-5:])

# --- Exercise 2 ---
# Task: Given a messy string, clean it up by stripping whitespace
# and converting it to title case.
print("\nExercise 2: clean up a messy string")
messy = "   the bhagavad gita   "
cleaned = messy.strip().title()
print(f"Cleaned: '{cleaned}'")

# --- Exercise 3 ---
# Task: Count how many times the letter "a" appears in "Bhagavad Gita"
# (case-insensitive).
print("\nExercise 3: count a letter, ignoring case")
text = "Bhagavad Gita"
count_a = text.lower().count("a")
print(f"'a' appears {count_a} times")

# --- Exercise 4 ---
# Task: Check whether the word "Krishna" is found inside a sentence.
print("\nExercise 4: check if a word exists in a sentence")
sentence = "Krishna spoke wisdom to Arjuna on the battlefield"
found = "Krishna" in sentence   # the "in" keyword checks membership
print("Is 'Krishna' in the sentence?", found)


print()
print("=" * 60)
print("PART 7: REAL WORLD EXAMPLE - BHAGAVAD GITA VERSE ANALYSIS")
print("=" * 60)

verse = "  Karmanye vadhikaraste Ma Phaleshu Kadachana  "

# Step 1: clean the raw text (real data is often messy with extra spaces)
clean_verse = verse.strip()
print(f"Cleaned verse: '{clean_verse}'")

# Step 2: break it into individual words
verse_words = clean_verse.split()
print("Words:", verse_words)

# Step 3: find how many words start with a capital letter
capitalized_words = [w for w in verse_words if w[0].isupper()]
print("Capitalized words:", capitalized_words)

# Step 4: build a readable summary using an f-string
print(f"\nThis verse has {len(verse_words)} words, "
      f"and the longest word is '{max(verse_words, key=len)}'.")
