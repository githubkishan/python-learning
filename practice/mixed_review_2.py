"""
practice/mixed_review_2.py

A tougher mixed-review set, one level up from practice/exercises.py.
These combine ideas across variables, strings, lists, dictionaries,
loops, functions, OOP, exceptions, file handling, and recursion.
Try each one yourself before reading the solution underneath it!

Run this file with:  python practice/mixed_review_2.py
"""

print("=" * 60)
print("CHALLENGE 1: Word frequency counter")
print("=" * 60)
# Task: Count how many times each word appears in a passage,
# ignoring case and punctuation, then print the 3 most common words.

import string

passage = (
    "Do your duty duty without attachment. Duty done without attachment "
    "brings peace. Peace comes from letting go of attachment to results."
)

# Remove punctuation and lowercase everything before counting
cleaned = passage.translate(str.maketrans("", "", string.punctuation)).lower()
words = cleaned.split()

word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# sorted() with key=lambda lets us rank the dictionary by count
top_words = sorted(word_counts.items(), key=lambda pair: pair[1], reverse=True)[:3]
print("Top 3 words:", top_words)


print()
print("=" * 60)
print("CHALLENGE 2: Group chapters by verse-count range")
print("=" * 60)
# Task: Sort chapters into "short" (<30), "medium" (30-59), and
# "long" (60+) groups based on their verse count.

chapters = [
    {"number": 1, "verses": 47}, {"number": 2, "verses": 72},
    {"number": 6, "verses": 47}, {"number": 12, "verses": 20},
    {"number": 15, "verses": 20}, {"number": 18, "verses": 78},
]

groups = {"short": [], "medium": [], "long": []}
for chapter in chapters:
    verses = chapter["verses"]
    if verses < 30:
        groups["short"].append(chapter["number"])
    elif verses < 60:
        groups["medium"].append(chapter["number"])
    else:
        groups["long"].append(chapter["number"])

for label, chapter_numbers in groups.items():
    print(f"{label}: {chapter_numbers}")


print()
print("=" * 60)
print("CHALLENGE 3: A quiz-scoring class with a history log")
print("=" * 60)
# Task: Build a class that records every quiz attempt and can
# report the best score and the average score so far.

class QuizHistory:
    def __init__(self):
        self.attempts = []   # a list of past scores

    def record(self, score):
        self.attempts.append(score)

    def best_score(self):
        return max(self.attempts) if self.attempts else None

    def average_score(self):
        if not self.attempts:
            return 0
        return round(sum(self.attempts) / len(self.attempts), 1)

history = QuizHistory()
for score in [4, 7, 6, 9, 5]:
    history.record(score)

print("All attempts:", history.attempts)
print("Best score:", history.best_score())
print("Average score:", history.average_score())


print()
print("=" * 60)
print("CHALLENGE 4: Safely parse a batch of answers")
print("=" * 60)
# Task: Given a list of raw answer strings (some invalid), return
# a list of valid integers only, using exception handling instead
# of crashing on the bad ones.

raw_answers = ["2", "4", "oops", "1", "", "3", "9"]

def parse_valid_answers(raw_list, min_value=1, max_value=4):
    valid = []
    for raw in raw_list:
        try:
            value = int(raw)
        except ValueError:
            continue   # skip anything that isn't a number at all
        if min_value <= value <= max_value:
            valid.append(value)
    return valid

print("Valid answers:", parse_valid_answers(raw_answers))


print()
print("=" * 60)
print("CHALLENGE 5: Flatten a nested list recursively")
print("=" * 60)
# Task: Given a list that contains numbers and other lists mixed
# together, "flatten" it into one single list with no nesting.

nested = [1, [2, 3, [4, 5]], 6, [7, [8, [9, 10]]]]

def flatten(data):
    result = []
    for item in data:
        if isinstance(item, list):
            result.extend(flatten(item))   # recurse, then merge the result in
        else:
            result.append(item)
    return result

print("Flattened:", flatten(nested))


print()
print("=" * 60)
print("CHALLENGE 6: Save and reload quiz results with file handling")
print("=" * 60)
# Task: Save a list of quiz scores to a file as comma-separated
# values, then read them back and compute the average - combining
# file handling with the kind of parsing from Challenge 4.

import os

demo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp_scores.txt")

scores_to_save = [8, 6, 9, 7]
with open(demo_path, "w") as f:
    f.write(",".join(str(s) for s in scores_to_save))

with open(demo_path, "r") as f:
    loaded_scores = [int(s) for s in f.read().split(",")]

print("Loaded scores:", loaded_scores)
print("Average:", round(sum(loaded_scores) / len(loaded_scores), 2))

os.remove(demo_path)   # clean up so re-running this file stays tidy


print()
print("=" * 60)
print("CHALLENGE 7: Bringing it all together - a shloka study session")
print("=" * 60)
# Task: Combine a class, a loop, exception handling, and f-strings
# to simulate a short study session with validated self-ratings.

class StudySession:
    def __init__(self):
        self.ratings = {}   # maps "chapter.verse" -> confidence rating (1-5)

    def rate(self, chapter, verse, raw_rating):
        key = f"{chapter}.{verse}"
        try:
            rating = int(raw_rating)
        except ValueError:
            print(f"  Skipping {key}: '{raw_rating}' is not a valid rating.")
            return
        if not (1 <= rating <= 5):
            print(f"  Skipping {key}: rating must be between 1 and 5.")
            return
        self.ratings[key] = rating
        print(f"  Recorded {key} with confidence {rating}/5.")

    def weakest_verses(self, threshold=3):
        return [key for key, rating in self.ratings.items() if rating < threshold]

session = StudySession()
practice_data = [(2, 47, "5"), (2, 20, "2"), (6, 5, "nine"), (18, 66, "1")]

print("Logging today's study session:")
for chapter, verse, raw_rating in practice_data:
    session.rate(chapter, verse, raw_rating)

print(f"\nVerses that need more review: {session.weakest_verses()}")
