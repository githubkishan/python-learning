"""
gita_quiz.py

An interactive terminal quiz about the Bhagavad Gita. Read a
shloka, pick the meaning that matches it from 4 options, and
see how many of 10 rounds you can get right. Beat your saved
high score to level up your rank!

Run it with:  python gita_quiz.py
"""

import os
import random

from shlokas import SHLOKAS

SCORE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scores.txt")
QUESTIONS_PER_ROUND = 10
OPTIONS_PER_QUESTION = 4

# Score thresholds (out of QUESTIONS_PER_ROUND) mapped to a fun title.
# Checked from highest to lowest, so the first match wins.
RANKS = [
    (9, "Enlightened Sage \U0001F9D8"),
    (7, "Devoted Scholar \U0001F4FF"),
    (5, "Sincere Seeker \U0001F331"),
    (0, "Curious Beginner \U0001F530"),
]


def print_banner():
    print("=" * 60)
    print("BHAGAVAD GITA SHLOKA QUIZ")
    print("=" * 60)
    print("Read each shloka and pick the option that best matches its meaning.")
    print(f"You'll be asked {QUESTIONS_PER_ROUND} questions. Let's begin!\n")


def build_question(correct_shloka, all_shlokas):
    """Turn one shloka into a shuffled multiple-choice question."""
    wrong_pool = [s for s in all_shlokas if s is not correct_shloka]
    wrong_choices = random.sample(wrong_pool, OPTIONS_PER_QUESTION - 1)

    options = [correct_shloka] + wrong_choices
    random.shuffle(options)
    correct_index = options.index(correct_shloka)
    return options, correct_index


def get_valid_answer():
    """Keep asking until the player types 1-4, or input runs out."""
    while True:
        try:
            raw = input(f"Your answer (1-{OPTIONS_PER_QUESTION}): ").strip()
        except EOFError:
            return None
        if raw.isdigit() and 1 <= int(raw) <= OPTIONS_PER_QUESTION:
            return int(raw)
        print(f"Please enter a number between 1 and {OPTIONS_PER_QUESTION}.")


def ask_question(number, shloka, all_shlokas):
    """Print one question, collect an answer, and report if it was correct."""
    options, correct_index = build_question(shloka, all_shlokas)

    print(f"Q{number}. Chapter {shloka['chapter']}, Verse {shloka['verse']}")
    print(f'    "{shloka["sanskrit"]}"\n')
    print("What does this shloka mean?")
    for i, option in enumerate(options, start=1):
        print(f"  {i}. {option['meaning']}")

    answer = get_valid_answer()
    if answer is None:
        return None   # input ran out - let the caller end the quiz early

    is_correct = (answer - 1) == correct_index
    if is_correct:
        print("Correct! \U00002705\n")
    else:
        print(f"Not quite \U0000274C. The right answer was: {options[correct_index]['meaning']}\n")
    return is_correct


def get_rank(score):
    for threshold, title in RANKS:
        if score >= threshold:
            return title
    return RANKS[-1][1]


def load_high_score():
    if not os.path.exists(SCORE_FILE):
        return 0
    with open(SCORE_FILE, "r") as f:
        contents = f.read().strip()
    return int(contents) if contents.isdigit() else 0


def save_high_score(score):
    with open(SCORE_FILE, "w") as f:
        f.write(str(score))


def show_results(score, total):
    print("=" * 60)
    print(f"QUIZ COMPLETE! You scored {score}/{total}")
    print(f"Rank: {get_rank(score)}")

    high_score = load_high_score()
    if score > high_score:
        save_high_score(score)
        print(f"New high score! \U0001F389 Previous best was {high_score}/{QUESTIONS_PER_ROUND}.")
    else:
        print(f"Your high score is still {high_score}/{QUESTIONS_PER_ROUND}. Try again!")
    print("=" * 60)


def run_quiz():
    print_banner()

    round_shlokas = random.sample(SHLOKAS, QUESTIONS_PER_ROUND)
    score = 0
    answered = 0

    for i, shloka in enumerate(round_shlokas, start=1):
        result = ask_question(i, shloka, SHLOKAS)
        if result is None:
            print("\n(No more input received - ending the quiz early.)")
            break
        answered += 1
        if result:
            score += 1

    show_results(score, answered)


if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        print("\n\nQuiz interrupted. Hare Krishna! \U0001F64F")
