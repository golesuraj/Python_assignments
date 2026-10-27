print("=" * 55)
print("              PYTHON GENERAL KNOWLEDGE QUIZ")
print("=" * 55)
print("Answer the following 5 questions to test your knowledge.\n")

quiz_data = [
    {
        "question": "1. What is the keyword used to define a function in Python?",
        "answer": "def"
    },
    {
        "question": "2. Which data type is immutable: list or tuple?",
        "answer": "tuple"
    },
    {
        "question": "3. Which loop is used when the number of iterations is known in advance (for/while)?",
        "answer": "for"
    },
    {
        "question": "4. What is the output function used to display messages on screen in Python?",
        "answer": "print"
    },
    {
        "question": "5. What statement is used to exit immediately from a loop in Python?",
        "answer": "break"
    }
]

score = 0
total_questions = len(quiz_data)

for item in quiz_data:
    print(item["question"])
    user_answer = input("Your answer: ").strip().lower()

    if user_answer == item["answer"].lower():
        print(">> Correct! (+1 point)\n")
        score += 1
    else:
        print(f">> Incorrect! The correct answer was: {item['answer']}\n")

percentage = (score / total_questions) * 100

if percentage >= 80:
    performance_message = "Excellent"
elif percentage >= 60:
    performance_message = "Good"
else:
    performance_message = "Keep Practicing"

print("=" * 55)
print("                 QUIZ RESULT")
print("=" * 55)
print(f"Total Questions     : {total_questions}")
print(f"Correct Answers     : {score}")
print(f"Score Percentage    : {percentage:.1f}%")
print(f"Performance Status  : {performance_message}")
print("=" * 55)
