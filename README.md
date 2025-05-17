-- Anshika Sharma 

INSTRUCTIONS

Once you are done with your code. Push your code to your github account
Make the repository public. Write a Readme for installation/running or any other information
Test if it's accessible publicly.
Share the repository link in the google form provided

PROBLEM STATEMENT
You are building the backend for a smart flashcard system. Users can add flashcards with just a question and answer — no subject is specified by them. Your backend will automatically determine the subject of the flashcard based on the text (e.g., presence of keywords like "photosynthesis" → "Biology").
Later, a student can request flashcards from any subject, and your API should return a mixed batch intelligently.
Task 1: Add Flashcard with Subject Inference
Endpoint:
POST /flashcard
{
  "student_id": "stu001",
  "question": "What is Newton's Second Law?",
  "answer": "Force equals mass times acceleration"
}

Output:
{
  "message": "Flashcard added successfully",
  "subject": "Physics"
}

Use any method that you want for classification logic:
Option 1 Can be Rule-based :
Option 2 Any Pre-trained model or trained model:

If you are training the model, you need to figure out the data


Requirements:
Detect the subject of the flashcard (e.g., "Physics") based on the question.


Store student_id, question, answer, and subject.

Task 2: Get Flashcards by Mixed Subjects
Endpoint:
GET /get-subject?student_id=stu001&limit=5

Output:.
[
  {
	"question": "What is Newton's Second Law?",
	"answer": "Force equals mass times acceleration",
	"subject": "Physics"
  },
  {
	"question": "What is photosynthesis?",
	"answer": "A process used by plants to convert light into energy",
	"subject": "Biology"
  }
]

Behavior:
Return up to limit number of flashcards from different subjects.


Shuffle to mix subjects.


Only return flashcards for the given student

INSTALLATION

pip install fastapi uvicorn