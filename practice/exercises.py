"""
practice/exercises.py

A mixed practice set pulling together everything from 01_basics
and 02_loops_functions: variables, strings, lists, dictionaries,
loops, and functions. Each exercise has a solution right below it -
try solving it yourself first before reading the solution!

Run this file with:  python practice/exercises.py
"""

print("=" * 60)
print("EXERCISE 1: Variables and f-strings")
print("=" * 60)
# Task: Store your name and favorite Bhagavad Gita chapter number
# in variables, then print a sentence using an f-string.

name = "Kishan"
favorite_chapter = 2
print(f"{name}'s favorite chapter is Chapter {favorite_chapter}.")


print()
print("=" * 60)
print("EXERCISE 2: String manipulation")
print("=" * 60)
# Task: Given a shloka title in mixed case with extra spaces,
# clean it up and make it consistent (title case, no extra spaces).

raw_title = "   the BHAGAVAD gita   "
clean_title = raw_title.strip().title()
print(f"Raw:   '{raw_title}'")
print(f"Clean: '{clean_title}'")


print()
print("=" * 60)
print("EXERCISE 3: List filtering and sorting")
print("=" * 60)
# Task: Given a list of chapter verse counts, sort them and print
# only the chapters with more than 30 verses, from largest to smallest.

verse_counts = [47, 72, 43, 20, 19, 24, 35]
long_chapters = [v for v in verse_counts if v > 30]
long_chapters_sorted = sorted(long_chapters, reverse=True)
print("Chapters with more than 30 verses (largest first):", long_chapters_sorted)


print()
print("=" * 60)
print("EXERCISE 4: Dictionary lookup with a default")
print("=" * 60)
# Task: Given a dictionary of chapter names by number, look up a
# chapter that may or may not exist, with a friendly fallback message.

chapter_names = {1: "Arjuna Vishada Yoga", 2: "Sankhya Yoga", 3: "Karma Yoga"}

def get_chapter_name(number):
    return chapter_names.get(number, f"Chapter {number} is not in our records yet")

print(get_chapter_name(2))
print(get_chapter_name(10))


print()
print("=" * 60)
print("EXERCISE 5: Loops with counters")
print("=" * 60)
# Task: Count how many chapters (out of 1-18) have an even number,
# using a for loop.

even_chapter_count = 0
for chapter in range(1, 19):
    if chapter % 2 == 0:
        even_chapter_count += 1
print(f"Number of even-numbered chapters (1-18): {even_chapter_count}")


print()
print("=" * 60)
print("EXERCISE 6: Functions that return values")
print("=" * 60)
# Task: Write a function that takes a list of verse counts and returns
# a dictionary summary: total, average, longest, shortest.

def summarize_verses(verse_counts):
    """Return a dictionary with total, average, longest, and shortest verse counts."""
    return {
        "total": sum(verse_counts),
        "average": round(sum(verse_counts) / len(verse_counts), 1),
        "longest": max(verse_counts),
        "shortest": min(verse_counts),
    }

summary = summarize_verses([47, 72, 43, 20, 19])
print("Summary:", summary)
print(f"On average, chapters have {summary['average']} verses.")


print()
print("=" * 60)
print("EXERCISE 7: Combining lists and dictionaries")
print("=" * 60)
# Task: Given a list of shloka dictionaries, build a NEW dictionary
# that maps "chapter.verse" -> meaning, using a loop.

gita_shlokas = [
    {"chapter": 2, "verse": 47, "meaning": "Focus on your actions, not the results."},
    {"chapter": 2, "verse": 20, "meaning": "The soul is never born, and it never dies."},
    {"chapter": 6, "verse": 5, "meaning": "Lift yourself up by your own efforts."},
]

verse_lookup = {}
for shloka in gita_shlokas:
    key = f"{shloka['chapter']}.{shloka['verse']}"
    verse_lookup[key] = shloka["meaning"]

print("Built lookup table:", verse_lookup)
print("Looking up 2.47:", verse_lookup["2.47"])


print()
print("=" * 60)
print("EXERCISE 8: A mini quiz function")
print("=" * 60)
# Task: Write a function that checks a user's answer (case-insensitive,
# ignoring extra spaces) against the correct answer and returns a
# friendly True/False style message.

def check_answer(user_answer, correct_answer):
    """Compare two answers loosely (ignore case and extra spaces)."""
    cleaned_user = user_answer.strip().lower()
    cleaned_correct = correct_answer.strip().lower()
    return cleaned_user == cleaned_correct

question = "Who spoke the Bhagavad Gita to Arjuna?"
correct_answer = "Krishna"
user_answer = "  krishna  "

print("Question:", question)
if check_answer(user_answer, correct_answer):
    print("Correct! Well done.")
else:
    print(f"Not quite. The correct answer is '{correct_answer}'.")


print()
print("=" * 60)
print("EXERCISE 9: Bringing it all together - a mini report")
print("=" * 60)
# Task: Use variables, a loop, a function, and f-strings together to
# print a short "study report" for a list of chapters read so far.

chapters_read = [
    {"number": 1, "name": "Arjuna Vishada Yoga", "verses": 47},
    {"number": 2, "name": "Sankhya Yoga", "verses": 72},
    {"number": 3, "name": "Karma Yoga", "verses": 43},
]

def build_report(chapters):
    """Print a formatted study report for a list of chapter dictionaries."""
    print(f"Study Report - {len(chapters)} chapters completed")
    print("-" * 40)
    for chapter in chapters:
        print(f"  Ch.{chapter['number']} {chapter['name']} "
              f"- {chapter['verses']} verses")
    total = sum(chapter["verses"] for chapter in chapters)
    print("-" * 40)
    print(f"Total verses read: {total}")

build_report(chapters_read)
