import json

def load_questions(filename="python_quiz.json"):
    with open(filename, "r") as file:
        return json.load(file)

def run_quiz(questions):
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['question']}")
        for idx, option in enumerate(q['options'], 1):
            print(f"  {idx}. {option}")
        try:
            answer = int(input("Enter option number: "))
            if q['options'][answer - 1].lower() == q['answer'].lower():
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}")
        except (ValueError, IndexError):
            print(f"❌ Invalid input! Correct answer: {q['answer']}")
    return score

def main():
    questions = load_questions()
    print("🐍 Welcome to the Python Quiz Game!")
    print("----------------------------------")
    score = run_quiz(questions)
    print("\n----------------------------------")
    print(f"Your Final Score: {score}/{len(questions)}")
    if score == len(questions):
        print("🏆 Excellent! You are a Python Pro!")
    elif score >= len(questions) // 2:
        print("👍 Good job, keep learning Python!")
    else:
        print("💡 Keep practicing, you’ll get better!")

if __name__ == "__main__":
    main()