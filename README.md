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
