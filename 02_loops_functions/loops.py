"""
02_loops_functions/loops.py

Loops let you repeat an action without writing the same code
over and over. Covers for loops, while loops, range(), break,
continue, enumerate(), and zip().

Run this file with:  python 02_loops_functions/loops.py
"""

print("=" * 60)
print("PART 1: THE FOR LOOP")
print("=" * 60)

# A "for" loop walks through each item in a collection, one at a time.
chapters = ["Karma Yoga", "Jnana Yoga", "Bhakti Yoga"]
for chapter in chapters:
    print("Chapter:", chapter)

# range(start, stop, step) generates a sequence of numbers.
# stop is NOT included, just like with slicing.
print("\nrange(5):")
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

print("\nrange(1, 19):  (Bhagavad Gita has 18 chapters)")
for chapter_number in range(1, 19):
    pass   # "pass" means "do nothing" - a placeholder for empty code
print("Looped through chapters 1 to 18 silently (used 'pass').")


print()
print("=" * 60)
print("PART 2: THE WHILE LOOP")
print("=" * 60)

# A "while" loop repeats AS LONG AS a condition stays True.
# You must update the condition inside the loop, or it runs forever!
chapters_read = 0
total_chapters = 5
while chapters_read < total_chapters:
    chapters_read += 1   # same as: chapters_read = chapters_read + 1
    print(f"Read chapter {chapters_read} of {total_chapters}")


print()
print("=" * 60)
print("PART 3: BREAK AND CONTINUE")
print("=" * 60)

# "break" -> stops the loop completely, right away
print("Using break: stop as soon as we find chapter 3")
for chapter_number in range(1, 10):
    if chapter_number == 3:
        break
    print("Checking chapter", chapter_number)

# "continue" -> skips the rest of THIS loop cycle, then moves to the next one
print("\nUsing continue: skip even chapter numbers")
for chapter_number in range(1, 8):
    if chapter_number % 2 == 0:
        continue
    print("Odd chapter:", chapter_number)


print()
print("=" * 60)
print("PART 4: ENUMERATE() - GET INDEX + VALUE TOGETHER")
print("=" * 60)

# enumerate() gives you both the position (index) and the value
# while looping - very handy for numbered lists.
teachings = ["Do your duty", "Let go of attachment", "Seek inner peace"]
for index, teaching in enumerate(teachings):
    print(f"{index + 1}. {teaching}")   # +1 so counting starts at 1, not 0


print()
print("=" * 60)
print("PART 5: ZIP() - LOOP THROUGH TWO LISTS TOGETHER")
print("=" * 60)

# zip() pairs up items from two (or more) lists by position.
chapter_names = ["Karma Yoga", "Jnana Yoga", "Bhakti Yoga"]
verse_counts = [43, 72, 29]

for name, count in zip(chapter_names, verse_counts):
    print(f"{name} has {count} verses")


print()
print("=" * 60)
print("PART 6: NESTED LOOPS")
print("=" * 60)

# A loop inside another loop - useful for grid-like data.
groups = {
    "Karma-focused": ["Karma Yoga", "Sankhya Yoga"],
    "Devotion-focused": ["Bhakti Yoga", "Raja Vidya Yoga"],
}
for group_name, group_chapters in groups.items():
    print(f"{group_name}:")
    for chapter in group_chapters:
        print(f"  - {chapter}")


print()
print("=" * 60)
print("PART 7: PRACTICE EXERCISES WITH SOLUTIONS")
print("=" * 60)

# --- Exercise 1 ---
# Task: Print all numbers from 1 to 10 using a while loop.
print("\nExercise 1: count to 10 with a while loop")
count = 1
while count <= 10:
    print(count, end=" ")
    count += 1
print()   # move to a new line after the loop

# --- Exercise 2 ---
# Task: Use a for loop with break to find the first verse count
# in a list that is greater than 50.
print("\nExercise 2: find the first value over 50")
verse_counts = [47, 20, 5, 72, 11]
for count in verse_counts:
    if count > 50:
        print("First chapter with over 50 verses has:", count)
        break

# --- Exercise 3 ---
# Task: Use enumerate() to print each chapter with a 1-based
# chapter number.
print("\nExercise 3: number a list with enumerate()")
chapters = ["Arjuna Vishada Yoga", "Sankhya Yoga", "Karma Yoga"]
for i, chapter in enumerate(chapters, start=1):   # start=1 skips the +1 math
    print(f"Chapter {i}: {chapter}")

# --- Exercise 4 ---
# Task: Use a for loop to sum only the even numbers from 1 to 20.
print("\nExercise 4: sum even numbers with continue")
even_sum = 0
for n in range(1, 21):
    if n % 2 != 0:
        continue
    even_sum += n
print("Sum of even numbers 1-20:", even_sum)


print()
print("=" * 60)
print("PART 8: REAL WORLD EXAMPLE - BHAGAVAD GITA READING TRACKER")
print("=" * 60)

# Simulating a daily reading plan: read a few verses each day
# until the whole chapter is finished.
total_verses_in_chapter = 47
verses_per_day = 10
day = 0
verses_read = 0

while verses_read < total_verses_in_chapter:
    day += 1
    # min() makes sure we don't "read" more verses than actually remain
    today_reading = min(verses_per_day, total_verses_in_chapter - verses_read)
    verses_read += today_reading
    print(f"Day {day}: read {today_reading} verses "
          f"(total so far: {verses_read}/{total_verses_in_chapter})")

print(f"\nFinished the chapter in {day} days!")

# Loop through named shlokas and stop early once we reach a target theme
gita_shlokas = [
    {"chapter": 2, "verse": 47, "theme": "duty"},
    {"chapter": 2, "verse": 20, "theme": "soul"},
    {"chapter": 6, "verse": 5, "theme": "self-effort"},
]
print("\nSearching for the 'soul' themed shloka:")
for shloka in gita_shlokas:
    if shloka["theme"] == "soul":
        print(f"Found it: Chapter {shloka['chapter']}, Verse {shloka['verse']}")
        break
