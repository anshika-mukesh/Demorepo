"""
This module contains the logic to infer the subject of a flashcard
based on rule-based keyword matching.
"""

def infer_subject(text: str) -> str:
    """
    Infers the subject of the flashcard based on keywords in the question text.

    Args:
        text (str): The question text from the flashcard.

    Returns:
        str: The inferred subject, e.g., "Physics", "Biology".
    """
    text = text.lower()
    keywords = {
        "Physics": ["force", "acceleration", "velocity", "newton", "gravity", "energy"],
        "Biology": ["photosynthesis", "cell", "organism", "plant", "enzyme", "mitochondria"],
        "Chemistry": ["atom", "molecule", "reaction", "acid", "base", "compound"],
        "Math": ["algebra", "geometry", "equation", "derivative", "integral", "calculus"],
        "History": ["war", "revolution", "empire", "ancient", "medieval", "treaty"],
        "Geography": ["continent", "river", "mountain", "ocean", "climate", "desert"]
    }

    for subject, terms in keywords.items():
        if any(word in text for word in terms):
            return subject
    return "General"
