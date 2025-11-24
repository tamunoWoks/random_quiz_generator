# Import necessary modules:
from pathlib import Path
import random
from typing import Dict, List

CAPITALS: Dict[str, str] = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
    'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
    'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
    'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
    'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
    'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
    'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}

OUTPUT_DIR = Path("quizzes")

def get_answer_options(correct: str, all_capitals: List[str]) -> List[str]:
    # Return 4 answer options with 1 correct + 3 random wrong answers.
    wrong_answers = random.sample([c for c in all_capitals if c != correct], 3)
    options = wrong_answers + [correct]
    random.shuffle(options)
    return options

def write_quiz(quiz_path: Path, states: List[str], all_capitals: List[str]):
    # Write one quiz file.
    with quiz_path.open('w', encoding='utf-8') as f:
        f.write("Name:\n\nDate:\n\nPeriod:\n\n")
        f.write(f"{' ' * 20}State Capitals Quiz ({quiz_path.stem})\n\n")

        for i, state in enumerate(states, start=1):
            correct = CAPITALS[state]
            options = get_answer_options(correct, all_capitals)

            f.write(f"{i}. What is the capital of {state}?\n")
            for letter, option in zip("ABCD", options):
                f.write(f"    {letter}. {option}\n")
            f.write("\n")
