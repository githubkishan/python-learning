"""
practice/file_handling.py

File handling: how to read from and write to files on disk, so
your programs can save data that survives after they finish
running. Covers open(), the "with" statement, reading/writing
text, appending, and working with simple CSV-style data.

This file creates and cleans up its own temporary files as it
runs, so it's completely safe to execute as many times as you like.

Run this file with:  python practice/file_handling.py
"""

import os

# Keep all demo files inside a folder next to this script so nothing
# leaks into the rest of the repo.
DEMO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "file_demo")
os.makedirs(DEMO_DIR, exist_ok=True)


print("=" * 60)
print("PART 1: WRITING TO A FILE")
print("=" * 60)

# "with open(...) as f" is the standard way to work with files in
# Python - it automatically closes the file for you, even if an
# error happens while you're using it.
notes_path = os.path.join(DEMO_DIR, "notes.txt")

with open(notes_path, "w") as f:   # "w" = write mode (overwrites the file)
    f.write("Favorite shloka: Bhagavad Gita 2.47\n")
    f.write("Theme: duty without attachment\n")

print(f"Wrote notes to {notes_path}")


print()
print("=" * 60)
print("PART 2: READING A FILE")
print("=" * 60)

# "r" = read mode. .read() grabs the ENTIRE file as one string.
with open(notes_path, "r") as f:
    contents = f.read()

print("Full file contents:")
print(contents)

# You can also read a file line by line, which is often more useful
with open(notes_path, "r") as f:
    print("Reading line by line:")
    for line in f:
        print("  ->", line.strip())   # .strip() removes the trailing newline


print()
print("=" * 60)
print("PART 3: APPENDING TO A FILE")
print("=" * 60)

# "a" = append mode. It adds new content to the END of the file
# instead of erasing what's already there.
with open(notes_path, "a") as f:
    f.write("Added later: Chapter 6 is about meditation.\n")

with open(notes_path, "r") as f:
    print("File after appending:")
    print(f.read())


print()
print("=" * 60)
print("PART 4: CHECKING IF A FILE EXISTS")
print("=" * 60)

# Always good practice to check before reading a file that might
# not exist yet, to avoid crashing with FileNotFoundError.
missing_path = os.path.join(DEMO_DIR, "does_not_exist.txt")

if os.path.exists(missing_path):
    print("File exists, safe to read.")
else:
    print(f"'{os.path.basename(missing_path)}' doesn't exist yet - skipping read.")


print()
print("=" * 60)
print("PART 5: WORKING WITH SIMPLE CSV-STYLE DATA")
print("=" * 60)

# A very common real-world task: saving a list of records as
# comma-separated lines, then reading them back into Python objects.
csv_path = os.path.join(DEMO_DIR, "chapters.csv")

chapters = [
    {"number": 1, "name": "Arjuna Vishada Yoga", "verses": 47},
    {"number": 2, "name": "Sankhya Yoga", "verses": 72},
    {"number": 3, "name": "Karma Yoga", "verses": 43},
]

with open(csv_path, "w") as f:
    for chapter in chapters:
        f.write(f"{chapter['number']},{chapter['name']},{chapter['verses']}\n")

print(f"Saved {len(chapters)} chapters to {os.path.basename(csv_path)}")

# Read the CSV-style file back and rebuild it as a list of dictionaries
loaded_chapters = []
with open(csv_path, "r") as f:
    for line in f:
        number, name, verses = line.strip().split(",")
        loaded_chapters.append({
            "number": int(number),
            "name": name,
            "verses": int(verses),
        })

print("Loaded back from file:")
for chapter in loaded_chapters:
    print(f"  Ch.{chapter['number']} {chapter['name']} - {chapter['verses']} verses")


print()
print("=" * 60)
print("PART 6: PRACTICE EXERCISES WITH SOLUTIONS")
print("=" * 60)

# --- Exercise 1 ---
# Task: Write a function that saves a list of strings to a file,
# one per line.
print("\nExercise 1: save a list of lines to a file")
def save_lines(path, lines):
    with open(path, "w") as f:
        for line in lines:
            f.write(line + "\n")

teachings_path = os.path.join(DEMO_DIR, "teachings.txt")
save_lines(teachings_path, ["Do your duty", "Let go of attachment", "Seek inner peace"])
print(f"Saved teachings to {os.path.basename(teachings_path)}")

# --- Exercise 2 ---
# Task: Write a function that reads a file and returns the number
# of lines in it, without crashing if the file doesn't exist.
print("\nExercise 2: safely count lines in a file")
def count_lines(path):
    if not os.path.exists(path):
        return 0
    with open(path, "r") as f:
        return len(f.readlines())

print(f"Lines in teachings.txt: {count_lines(teachings_path)}")
print(f"Lines in a missing file: {count_lines(os.path.join(DEMO_DIR, 'nope.txt'))}")

# --- Exercise 3 ---
# Task: Write a function that counts how many times a word appears
# across every line of a file.
print("\nExercise 3: count a word's occurrences in a file")
def count_word_in_file(path, word):
    count = 0
    with open(path, "r") as f:
        for line in f:
            count += line.lower().count(word.lower())
    return count

print(f"'duty' appears {count_word_in_file(teachings_path, 'duty')} time(s) in teachings.txt")


print()
print("=" * 60)
print("PART 7: REAL WORLD EXAMPLE - A SHLOKA JOURNAL")
print("=" * 60)

# A small "journal" feature: append a new reflection every time you
# study a shloka, then read back your full study history.
journal_path = os.path.join(DEMO_DIR, "shloka_journal.txt")

def add_journal_entry(chapter, verse, reflection):
    """Append one journal entry as a single line: chapter.verse: reflection"""
    with open(journal_path, "a") as f:
        f.write(f"{chapter}.{verse}: {reflection}\n")

def read_journal():
    """Return every journal entry as a list of strings."""
    if not os.path.exists(journal_path):
        return []
    with open(journal_path, "r") as f:
        return [line.strip() for line in f]

# Start fresh for this demo run
if os.path.exists(journal_path):
    os.remove(journal_path)

add_journal_entry(2, 47, "Reminded me to focus on effort, not outcome.")
add_journal_entry(6, 5, "Lifting myself up - no one else can do it for me.")

print("Journal entries so far:")
for entry in read_journal():
    print(" -", entry)


print()
print("=" * 60)
print("CLEANUP")
print("=" * 60)

# Clean up every demo file we created, so running this script
# repeatedly never leaves clutter behind.
for created_file in [notes_path, csv_path, teachings_path, journal_path]:
    if os.path.exists(created_file):
        os.remove(created_file)
os.rmdir(DEMO_DIR)
print("Removed all demo files. The repo is left exactly as it was.")
