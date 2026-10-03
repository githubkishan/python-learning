"""
practice/exceptions_handling.py

Exception handling: how to deal with errors gracefully instead of
letting your program crash. Covers try/except/else/finally, catching
specific error types, raising your own errors, and custom exceptions.

Run this file with:  python practice/exceptions_handling.py
"""

print("=" * 60)
print("PART 1: WHAT HAPPENS WITHOUT ERROR HANDLING")
print("=" * 60)

# Without handling, an error ("exception") stops your program completely.
# Try uncommenting the line below and running this file - it will crash:
# result = 10 / 0

print("(We're skipping the crash on purpose - see the comment above!)")


print()
print("=" * 60)
print("PART 2: TRY / EXCEPT")
print("=" * 60)

# "try" lets you attempt risky code. "except" catches the error if
# one happens, so your program can keep running.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught it! You can't divide by zero.")

# You can catch different error types differently
def get_chapter_name(chapters, index):
    try:
        return chapters[index]
    except IndexError:
        return "That chapter number doesn't exist."

chapters = ["Arjuna Vishada Yoga", "Sankhya Yoga", "Karma Yoga"]
print(get_chapter_name(chapters, 1))
print(get_chapter_name(chapters, 99))


print()
print("=" * 60)
print("PART 3: CATCHING MULTIPLE ERROR TYPES")
print("=" * 60)

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: cannot divide by zero"
    except TypeError:
        return "Error: both values must be numbers"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "two"))


print()
print("=" * 60)
print("PART 4: ELSE AND FINALLY")
print("=" * 60)

# "else" runs ONLY if no exception happened.
# "finally" ALWAYS runs, whether there was an error or not - great
# for cleanup code (like closing a file).
def read_verse_count(text):
    try:
        count = int(text)
    except ValueError:
        print(f"'{text}' is not a valid number.")
    else:
        print(f"Got a valid verse count: {count}")
    finally:
        print("Finished checking the input.\n")

read_verse_count("47")
read_verse_count("forty-seven")


print()
print("=" * 60)
print("PART 5: RAISING YOUR OWN EXCEPTIONS")
print("=" * 60)

# "raise" lets YOU trigger an error on purpose, usually to stop
# invalid data from going any further.
def set_chapter_number(number):
    if number < 1 or number > 18:
        raise ValueError("The Bhagavad Gita only has chapters 1 through 18.")
    return number

try:
    set_chapter_number(25)
except ValueError as error:
    print("Caught our own error:", error)


print()
print("=" * 60)
print("PART 6: CUSTOM EXCEPTIONS")
print("=" * 60)

# You can define your own exception types by creating a class
# that inherits from Exception. This makes error messages more
# specific and meaningful to your program.
class InvalidVerseError(Exception):
    """Raised when a verse number doesn't exist for a given chapter."""
    pass

def get_verse(chapter_verse_counts, chapter, verse):
    max_verses = chapter_verse_counts.get(chapter)
    if max_verses is None:
        raise InvalidVerseError(f"Chapter {chapter} does not exist.")
    if verse < 1 or verse > max_verses:
        raise InvalidVerseError(f"Chapter {chapter} only has {max_verses} verses.")
    return f"Chapter {chapter}, Verse {verse}"

chapter_verse_counts = {1: 47, 2: 72, 3: 43}

try:
    print(get_verse(chapter_verse_counts, 2, 90))
except InvalidVerseError as error:
    print("Invalid verse:", error)


print()
print("=" * 60)
print("PART 7: PRACTICE EXERCISES WITH SOLUTIONS")
print("=" * 60)

# --- Exercise 1 ---
# Task: Write a function that safely converts text to an integer,
# returning None instead of crashing if it fails.
print("\nExercise 1: safely convert text to a number")
def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None

print(safe_int("18"))
print(safe_int("eighteen"))

# --- Exercise 2 ---
# Task: Write a function that looks up a key in a dictionary and
# raises a custom error with a helpful message if it's missing.
print("\nExercise 2: raise a custom error for a missing key")
class MissingShlokaError(Exception):
    pass

def lookup_shloka(lookup, key):
    if key not in lookup:
        raise MissingShlokaError(f"No shloka found for '{key}'.")
    return lookup[key]

shloka_lookup = {"2.47": "Focus on your duty, not the results."}
try:
    print(lookup_shloka(shloka_lookup, "18.66"))
except MissingShlokaError as error:
    print("Caught:", error)

# --- Exercise 3 ---
# Task: Use try/except/finally to simulate "opening" and "closing"
# a resource even when something goes wrong in between.
print("\nExercise 3: guarantee cleanup with finally")
def process_chapter(chapter_number):
    print(f"Opening chapter {chapter_number}...")
    try:
        if chapter_number > 18:
            raise ValueError("No such chapter.")
        print(f"Reading chapter {chapter_number}...")
    except ValueError as error:
        print("Problem while reading:", error)
    finally:
        print(f"Closing chapter {chapter_number}.\n")

process_chapter(2)
process_chapter(99)


print()
print("=" * 60)
print("PART 8: REAL WORLD EXAMPLE - A SAFE SHLOKA QUIZ ANSWER CHECKER")
print("=" * 60)

# A realistic scenario: validating player input in a quiz, the same
# kind of thing gita_quiz.py (in the gita-quiz/ project) needs to do.
class InvalidAnswerError(Exception):
    """Raised when the player's answer isn't a valid option number."""
    pass

def validate_answer(raw_answer, num_options=4):
    try:
        answer = int(raw_answer)
    except ValueError:
        raise InvalidAnswerError(f"'{raw_answer}' is not a number.")

    if not (1 <= answer <= num_options):
        raise InvalidAnswerError(f"Answer must be between 1 and {num_options}.")

    return answer

test_inputs = ["2", "nine", "7", "4"]
for raw_input_value in test_inputs:
    try:
        validated = validate_answer(raw_input_value)
        print(f"'{raw_input_value}' is valid: chose option {validated}")
    except InvalidAnswerError as error:
        print(f"'{raw_input_value}' is invalid: {error}")
