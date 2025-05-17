"""
FastAPI app for a Smart Flashcard System with subject inference and retrieval.

Endpoints:
- POST /flashcard: Adds a new flashcard with automatic subject detection.
- GET /get-subject: Returns a shuffled mix of flashcards from different subjects for a student.
"""

from fastapi import FastAPI, Query
from pydantic import BaseModel
from subject_classifier import infer_subject
from storage import save_flashcard, get_flashcards_by_mixed_subjects

# Create FastAPI instance
app = FastAPI()


@app.get("/")
def read_root():
    """
    Root endpoint to verify the API is running.
    """
    return {"message": "Hello from Flashcard API"}


class Flashcard(BaseModel):
    student_id: str
    question: str
    answer: str


@app.post("/flashcard")
def add_flashcard(card: Flashcard):
    """
    Adds a flashcard for the given student and infers its subject.

    Request Body:
    {
        "student_id": "stu001",
        "question": "What is Newton's Second Law?",
        "answer": "Force equals mass times acceleration"
    }

    Returns:
        dict: Confirmation message and inferred subject.
    """
    # Infer the subject based on the question
    subject = infer_subject(card.question)

    # Create flashcard dictionary
    flashcard_data = {
        "student_id": card.student_id,
        "question": card.question,
        "answer": card.answer,
        "subject": subject
    }

    # Save flashcard
    save_flashcard(flashcard_data)

    return {"message": "Flashcard added successfully", "subject": subject}


@app.get("/get-subject")
def get_flashcards(student_id: str = Query(...), limit: int = Query(5)):
    """
    Retrieves a shuffled batch of flashcards for the student from different subjects.

    Query Parameters:
    - student_id: ID of the student
    - limit: Number of flashcards to return (default is 5)

    Returns:
        list: List of flashcards with mixed subjects.
    """
    return get_flashcards_by_mixed_subjects(student_id, limit)
