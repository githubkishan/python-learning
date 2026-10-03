"""
practice/oop_basics.py

Object-Oriented Programming (OOP): a way to organize code around
"objects" that bundle data (attributes) and behavior (methods)
together. Covers classes, objects, __init__, methods, and a first
look at inheritance.

Run this file with:  python practice/oop_basics.py
"""

print("=" * 60)
print("PART 1: YOUR FIRST CLASS")
print("=" * 60)

# A class is a blueprint for creating objects. Think of it like a
# cookie cutter - the class is the cutter, and each object you make
# from it is a cookie.
class Student:
    def __init__(self, name, favorite_subject):
        # __init__ runs automatically when you create a new Student.
        # "self" refers to the specific object being created.
        self.name = name
        self.favorite_subject = favorite_subject

    def introduce(self):
        # A method is just a function that belongs to a class.
        print(f"Hi, I'm {self.name} and I love studying {self.favorite_subject}.")

# Creating an object ("instance") from the Student class
student_one = Student("Kishan", "Python")
student_one.introduce()


print()
print("=" * 60)
print("PART 2: ATTRIBUTES CAN BE CHANGED")
print("=" * 60)

# Each object has its own copy of the attributes defined in __init__.
student_two = Student("Arjuna", "Dharma")
print(f"{student_one.name} loves {student_one.favorite_subject}")
print(f"{student_two.name} loves {student_two.favorite_subject}")

# You can read and update an attribute directly with dot notation
student_two.favorite_subject = "Yoga"
print(f"{student_two.name} now loves {student_two.favorite_subject}")


print()
print("=" * 60)
print("PART 3: METHODS THAT USE AND CHANGE DATA")
print("=" * 60)

class ChapterTracker:
    def __init__(self, total_chapters=18):
        self.total_chapters = total_chapters
        self.chapters_read = 0   # starts at zero

    def read_chapter(self):
        """Mark one more chapter as read, but don't go past the total."""
        if self.chapters_read < self.total_chapters:
            self.chapters_read += 1
        else:
            print("You've already finished every chapter!")

    def progress(self):
        """Return progress as a percentage."""
        return round((self.chapters_read / self.total_chapters) * 100, 1)

tracker = ChapterTracker()
tracker.read_chapter()
tracker.read_chapter()
tracker.read_chapter()
print(f"Chapters read: {tracker.chapters_read}/{tracker.total_chapters}")
print(f"Progress: {tracker.progress()}%")


print()
print("=" * 60)
print("PART 4: INHERITANCE - BUILDING ON AN EXISTING CLASS")
print("=" * 60)

# Inheritance lets a new class reuse everything from an existing
# class, then add or override behavior of its own.
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

class Devotee(Person):
    def __init__(self, name, favorite_deity):
        super().__init__(name)   # reuse Person's __init__ for "name"
        self.favorite_deity = favorite_deity

    def greet(self):
        # "Overriding" - this replaces Person's greet() for a Devotee
        print(f"Hare Krishna! I'm {self.name}, devoted to {self.favorite_deity}.")

regular_person = Person("Kishan")
regular_person.greet()

devotee = Devotee("Arjuna", "Krishna")
devotee.greet()


print()
print("=" * 60)
print("PART 5: PRACTICE EXERCISES WITH SOLUTIONS")
print("=" * 60)

# --- Exercise 1 ---
# Task: Create a Book class with title and author, and a method
# that prints a one-line description.
print("\nExercise 1: a simple Book class")
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(f"'{self.title}' by {self.author}")

book = Book("Bhagavad Gita As It Is", "A.C. Bhaktivedanta Swami")
book.describe()

# --- Exercise 2 ---
# Task: Give the Book class from Exercise 1 a "pages_read" attribute
# that starts at 0, and a method to add pages read.
print("\nExercise 2: track reading progress on an object")
class TrackedBook(Book):
    def __init__(self, title, author, total_pages):
        super().__init__(title, author)
        self.total_pages = total_pages
        self.pages_read = 0

    def read_pages(self, pages):
        self.pages_read = min(self.pages_read + pages, self.total_pages)

tracked_book = TrackedBook("Bhagavad Gita As It Is", "A.C. Bhaktivedanta Swami", 900)
tracked_book.read_pages(150)
tracked_book.read_pages(100)
print(f"Pages read: {tracked_book.pages_read}/{tracked_book.total_pages}")

# --- Exercise 3 ---
# Task: Write a class method that compares two objects' data and
# returns which one has made more progress.
print("\nExercise 3: compare two objects")
class Reader:
    def __init__(self, name, pages_read):
        self.name = name
        self.pages_read = pages_read

def who_read_more(reader_a, reader_b):
    if reader_a.pages_read > reader_b.pages_read:
        return reader_a.name
    elif reader_b.pages_read > reader_a.pages_read:
        return reader_b.name
    return "It's a tie!"

reader_a = Reader("Kishan", 250)
reader_b = Reader("Arjuna", 180)
print(f"Who read more? {who_read_more(reader_a, reader_b)}")


print()
print("=" * 60)
print("PART 6: REAL WORLD EXAMPLE - A BHAGAVAD GITA SHLOKA CLASS")
print("=" * 60)

# Modeling a shloka as a class instead of a plain dictionary lets us
# attach behavior (methods) directly to the data.
class Shloka:
    def __init__(self, chapter, verse, sanskrit, meaning):
        self.chapter = chapter
        self.verse = verse
        self.sanskrit = sanskrit
        self.meaning = meaning

    def reference(self):
        """Return a short 'chapter.verse' style reference string."""
        return f"{self.chapter}.{self.verse}"

    def display(self):
        print(f"Bhagavad Gita {self.reference()}")
        print(f"  Sanskrit: {self.sanskrit}")
        print(f"  Meaning : {self.meaning}")

class FavoriteShloka(Shloka):
    """A shloka the reader has marked as a personal favorite."""
    def __init__(self, chapter, verse, sanskrit, meaning, note):
        super().__init__(chapter, verse, sanskrit, meaning)
        self.note = note

    def display(self):
        super().display()   # reuse the parent's display, then add more
        print(f"  My note : {self.note}")

shloka = Shloka(
    chapter=2, verse=47,
    sanskrit="Karmanye vadhikaraste Ma Phaleshu Kadachana",
    meaning="You have the right to perform your duty, but never to the fruits of your actions.",
)
shloka.display()

print()
favorite = FavoriteShloka(
    chapter=2, verse=47,
    sanskrit="Karmanye vadhikaraste Ma Phaleshu Kadachana",
    meaning="You have the right to perform your duty, but never to the fruits of your actions.",
    note="This is the one I come back to whenever I feel anxious about results.",
)
favorite.display()

# A list of Shloka objects, just like we'd use a list of dictionaries
all_shlokas = [
    shloka,
    Shloka(2, 20, "Na jayate mriyate va kadachin", "The soul is never born, and it never dies."),
]
print(f"\nWe have {len(all_shlokas)} shlokas stored as objects:")
for s in all_shlokas:
    print(f"  - {s.reference()}: {s.meaning}")
