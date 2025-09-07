import json
from utils import load_json, save_json

QUESTIONS_FILE = "data/questions.json"
PROGRESS_FILE = "data/progress.json"

def select_category(questions):
    print("\nAvailable Categories:")
    for i, cat in enumerate(questions.keys(), start=1):
        print(f"{i}. {cat}")
    while True:
        choice = input("Select category number: ").strip()
        if not choice.isdigit():
            print("Enter a valid number.")
            continue
        choice = int(choice)
        if 1 <= choice <= len(questions):
            return list(questions.keys())[choice - 1]
        else:
            print("Choice out of range.")

def start_quiz(category, questions):
    score = 0
    for q in questions[category]:
        print("\n" + q["question"])
        for i, opt in enumerate(q["options"], start=1):
            print(f"{i}. {opt}")
        while True:
            ans = input("Your answer (number, 's' to skip): ").strip().lower()
            if ans == "s":
                print("⏭️ Question skipped")
                break
            if not ans.isdigit():
                print("Enter a valid number.")
                continue
            ans = int(ans)
            if ans < 1 or ans > len(q["options"]):
                print("Number out of range.")
                continue
            if q["options"][ans - 1].lower() == q["answer"].lower():
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}")
            break
    print(f"\n🎉 Your Score in {category}: {score}/{len(questions[category])}")
    return score

def update_progress(progress, user_id, user_name, category, score):
    if user_id not in progress:
        progress[user_id] = {"name": user_name, "scores": {}}
    if category not in progress[user_id]["scores"]:
        progress[user_id]["scores"][category] = []
    progress[user_id]["scores"][category].append(score)
    save_json(progress, PROGRESS_FILE)

def view_progress(progress, user_id):
    if user_id not in progress:
        print("📭 No progress yet for this user.")
        return
    print(f"\n📊 Progress for {progress[user_id]['name']}:")
    for cat, scores in progress[user_id]["scores"].items():
        avg = sum(scores)/len(scores)
        print(f"- {cat}: Attempts {len(scores)}, Average Score: {avg:.2f}")

def view_leaderboard(progress):
    print("\n🏆 Leaderboard:")
    leaderboard = []
    for user_id, data in progress.items():
        total_score = sum([sum(scores) for scores in data["scores"].values()])
        leaderboard.append((data["name"], total_score))
    leaderboard.sort(key=lambda x: x[1], reverse=True)
    for i, (name, score) in enumerate(leaderboard, start=1):
        print(f"{i}. {name} - Total Score: {score}")

def main():
    print("=== 🧠 Smart Quiz & Study Tracker ===")
    questions = load_json(QUESTIONS_FILE)
    progress = load_json(PROGRESS_FILE)

    while True:
        print("\nMenu:")
        print("1. Take Quiz")
        print("2. View Progress (by ID)")
        print("3. View Leaderboard")
        print("4. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            # Ask for user info before each quiz
            user_name = input("Enter your Name: ").strip()
            user_id = input("Enter your ID: ").strip()

            category = select_category(questions)
            score = start_quiz(category, questions)
            update_progress(progress, user_id, user_name, category, score)

        elif choice == "2":
            user_id = input("Enter your ID to view progress: ").strip()
            view_progress(progress, user_id)

        elif choice == "3":
            view_leaderboard(progress)

        elif choice == "4":
            print("💾 Progress saved. Goodbye!")
            save_json(progress, PROGRESS_FILE)
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
