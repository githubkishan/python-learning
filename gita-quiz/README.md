# 🕉️ Gita Quiz

A fun, interactive terminal quiz that tests how well you know the
meanings of shlokas (verses) from the Bhagavad Gita. Answer 10
random multiple-choice questions, get instant feedback, and try to
beat your saved high score!

## How to play

1. Make sure you have Python 3 installed:
   ```bash
   python3 --version
   ```
2. From the repo root, move into this folder and start the quiz:
   ```bash
   cd gita-quiz
   python3 gita_quiz.py
   ```
3. Each round shows you a shloka's chapter, verse, and Sanskrit line:
   ```
   Q1. Chapter 2, Verse 47
       "Karmanye vadhikaraste Ma Phaleshu Kadachana"

   What does this shloka mean?
     1. ...
     2. ...
     3. ...
     4. ...
   Your answer (1-4):
   ```
4. Type a number from **1 to 4** and press Enter. You'll immediately
   see ✅ if you're right, or ❌ with the correct answer if you're not.
5. After 10 questions, you'll get your final score and a rank:

   | Score (out of 10) | Rank |
   |---|---|
   | 9-10 | Enlightened Sage 🧘 |
   | 7-8  | Devoted Scholar 📿 |
   | 5-6  | Sincere Seeker 🌱 |
   | 0-4  | Curious Beginner 🔰 |

6. If you beat your previous best, it's saved automatically to
   `scores.txt` in this folder - so every playthrough is a chance to
   climb the ranks!

Press `Ctrl+C` at any time to quit early.

## Files in this project

| File | What it does |
|---|---|
| `gita_quiz.py` | The game itself: builds questions, tracks your score, saves your high score |
| `shlokas.py` | The question bank - 20 shlokas with chapter, verse, Sanskrit, and meaning |
| `scores.txt` | Auto-created after your first game to store your high score (not committed to git) |

## How the questions are built

Each round randomly picks 10 shlokas out of the 20 in `shlokas.py`.
For each one, the correct meaning is mixed in with 3 random wrong
meanings from other shlokas, then shuffled - so the correct answer
is never in the same position twice in a row.

## Running it in CI

`.github/workflows/gita-quiz.yml` plays a full automated round on
every change to this folder, so you can always see a sample run in
the workflow's summary tab on GitHub - no need to run it locally
just to see it in action.

Hare Krishna, and good luck! 🙏
