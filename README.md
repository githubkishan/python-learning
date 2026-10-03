# Python Learning Journey

A self-paced, beginner-friendly Python curriculum. Every file is a
standalone, runnable script with plain-English comments, practice
exercises with solutions, and real-world examples drawn from the
Bhagavad Gita.

Open `index.html` in your browser for a visual dashboard of the whole
curriculum, or just work through the files below in order.

## Structure

```
python-learning/
├── 01_basics/
│   ├── variables.py       # data types, string methods, f-strings
│   ├── strings.py         # indexing, slicing, immutability, more methods
│   ├── lists.py            # ordered collections, comprehensions, nesting
│   └── dictionaries.py    # key-value storage, lookups, nesting
├── 02_loops_functions/
│   ├── loops.py            # for/while, break/continue, enumerate, zip
│   └── functions.py       # def, defaults, *args/**kwargs, lambda, scope
├── 03_numpy/
│   └── numpy_basics.py    # arrays, vectorized math, stats, filtering
├── practice/
│   ├── exercises.py           # 9 mixed exercises across every topic
│   ├── oop_basics.py          # classes, objects, methods, inheritance
│   ├── exceptions_handling.py # try/except/finally, raising and custom errors
│   ├── file_handling.py       # reading/writing files, CSV-style data
│   ├── recursion_basics.py    # base cases, factorial, Fibonacci, nested data
│   └── mixed_review_2.py      # a tougher mixed-review set, combining every topic
├── gita-quiz/               # a separate interactive quiz project (see its own README)
├── index.html                # learning dashboard
└── README.md
```

## Getting started

You need Python 3 installed. Check with:

```bash
python3 --version
```

Run any lesson directly:

```bash
python3 01_basics/variables.py
python3 01_basics/strings.py
python3 01_basics/lists.py
python3 01_basics/dictionaries.py
python3 02_loops_functions/loops.py
python3 02_loops_functions/functions.py
python3 practice/exercises.py
python3 practice/oop_basics.py
python3 practice/exceptions_handling.py
python3 practice/file_handling.py
python3 practice/recursion_basics.py
python3 practice/mixed_review_2.py
```

The NumPy lesson needs one extra package first:

```bash
pip install numpy
python3 03_numpy/numpy_basics.py
```

## Suggested order

1. `01_basics/variables.py`
2. `01_basics/strings.py`
3. `01_basics/lists.py`
4. `01_basics/dictionaries.py`
5. `02_loops_functions/loops.py`
6. `02_loops_functions/functions.py`
7. `03_numpy/numpy_basics.py`
8. `practice/exercises.py` — review everything together

Each file follows the same pattern: a concept explained with comments,
a runnable example, then a "Practice Exercises" section with solutions,
and finally a real-world example so the concept sticks.
