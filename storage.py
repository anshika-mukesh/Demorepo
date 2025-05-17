"""
Handles flashcard data storage and retrieval using a JSON file.
"""

import json
import random
from pathlib import Path

FILE_PATH = Path("flashcards.json")

def load_flashcards():
    """
    Loads all flashcards from the JSON file.

    Returns:
        list: A list of flashcard dictionaries.
    """
    if FILE_PATH.exists():
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    return []

def save_flashcard(data: dict):
    """
    Appends a new flashcard to the JSON file.

    Args:
        data (dict): The flashcard data to store.
    """
    all_cards = load_flashcards()
    all_cards.append(data)
    with open(FILE_PATH, "w") as f:
        json.dump(all_cards, f, indent=2)

def get_flashcards_by_mixed_subjects(student_id: str, limit: int = 5):
    """
    Retrieves flashcards for a given student, mixing subjects up to the limit.

    Args:
        student_id (str): The student ID to filter flashcards.
        limit (int): Max number of flashcards to return.

    Returns:
        list: A list of flashcards with diverse subjects.
    """
    cards = load_flashcards()
    student_cards = [c for c in cards if c["student_id"] == student_id]

    # Group flashcards by subject
    subject_map = {}
    for card in student_cards:
        subject = card["subject"]
        subject_map.setdefault(subject, []).append(card)

    # Collect one flashcard from each subject
    mixed = []
    for subject_cards in subject_map.values():
        mixed.append(random.choice(subject_cards))
        if len(mixed) >= limit:
            break

    # If still under limit, fill with remaining cards
    if len(mixed) < limit:
        remaining = [c for c in student_cards if c not in mixed]
        random.shuffle(remaining)
        mixed += remaining[:limit - len(mixed)]

    random.shuffle(mixed)
    return mixed[:limit]
