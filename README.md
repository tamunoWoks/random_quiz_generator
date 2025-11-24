# Random Quiz Generator
This project contains two Python scripts that generate multiple-choice quizzes about U.S. state capitals. It includes:
1. **The original script** – a straightforward version based on the *Automate the Boring Stuff with Python* exercise.
2. **An improved, more Pythonic version** – rewritten for clarity, maintainability, and modern best practices.

This README explains how both scripts work, highlights their differences, and provides usage instructions.

### Overview:
These scripts automatically generate multiple randomized quiz files and answer keys. Each quiz contains 50 questions—one for each U.S. state—and each question presents four answer choices (A–D) in random order.  

The intended use case is educational: teachers can generate many different quiz versions so students cannot share answers easily.

## Script 1: The Original Version (`randomQuizGenerator.py`)
### Purpose:
The original script is a single-file procedural program that:
- Creates **35 quizzes**, each with **50 questions**.
- Randomizes the order of states.
- Generates 4 answer options for each question (1 correct + 3 wrong).
- Randomizes the option order.
- Creates matching answer key files.

### How It Works:
#### 1. Imports and Data Setup
The script imports `random` for shuffling and defines a large dictionary mapping states to capitals.

#### 2. Loop Over Quiz Count
A `for` loop runs 35 times, creating one quiz and one answer key per iteration.

#### 3. File Creation
For each quiz number:
- A quiz file named `capitalsquiz<n>.txt` is created.
- An answer key file named `capitalsquiz_answers<n>.txt` is created.

#### 4. Quiz Header
Each quiz starts with placeholders:
```
Name:

Date:

Period:
```
Followed by a centered quiz title.

#### 5. Randomizing Questions
The list of states is shuffled so each quiz has the questions in a different order.

#### 6. Creating Each Question
For each state:
- The correct capital is extracted.
- A list of all capitals is copied.
- The correct capital is removed.
- Three random wrong answers are selected.
- All four options are shuffled.
- The question and choices are written to the quiz file.
- The answer key file records the correct letter.

#### 7. Closing Files
Files are closed manually after writing.

### Strengths
- Simple and easy to understand.
- Achieves the goal effectively.

### Limitations
- Manual file handling instead of using context managers.
- Some repetitive logic.
- Harder to maintain or extend.
- Less modular.
- Output directory clutter.
- Minimal separation of concerns.
---

## Script 2: Improved & Pythonic Version (`randomQuizGenerator2.py`)
### Purpose:
This version rewrites the entire script to make it:
- Cleaner
- More modular
- Easier to read
- Easier to maintain
- More scalable
- More professional

### Key Improvements:
- Uses **functions** to separate logic.
- Uses **pathlib** for file paths.
- Uses **with open()** for automatic file handling.
- Ensures answer options are generated consistently.
- Supports easy modification (e.g., change number of quizzes).
- Stores output in a dedicated `quizzes/` directory.
- Adds **type hints** to improve clarity.
