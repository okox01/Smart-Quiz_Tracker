# 🧠 Smart Quiz & Study Tracker  

A Python command-line application that helps you **test your knowledge**, **track your progress**, and **compete on a leaderboard**.  
This project is designed as a beginner-friendly way to practice **Python basics** like loops, conditionals, file handling, and dictionaries — while building something fun and useful!  

---

## ✨ Features
- 📚 **Multiple Categories** – Choose from different quiz topics stored in `questions.json`.  
- 🎯 **Interactive Quiz** – Answer multiple-choice questions, skip if needed, and get instant feedback.  
- 📊 **Track Your Progress** – Progress is stored per user (by ID) in `progress.json`.  
- 🏆 **Leaderboard** – See who scored the highest across all attempts.  
- 💾 **Persistent Storage** – Uses JSON files for storing questions and tracking results.  

---

## 📂 Project Structure
project/
│── data/
│ ├── questions.json # Quiz questions
│ └── progress.json # User progress
│── utils.py # Helper functions (load/save JSON)
│── main.py # Main quiz application
│── README.md # Documentation

yaml
Copy code

---

## ⚙️ Installation & Setup
1. Clone this repository or download the files.  
   ```bash
   git clone <your-repo-url>
   cd project
Make sure you have Python 3.8+ installed.

Install any dependencies (if needed). For now, only Python standard library modules are used (json, os).

Run the app:

bash
Copy code
python main.py
🎮 How to Use
Start the program – You’ll see a menu:

markdown
Copy code
Menu:
1. Take Quiz
2. View Progress (by ID)
3. View Leaderboard
4. Exit
Take a quiz – Enter your name & ID, choose a category, and answer the questions.

Type the number of your answer.

Type s to skip a question.

Track your progress – Choose option 2, enter your ID, and see your attempts & average score.

View leaderboard – Choose option 3 to see who has the highest total score.

Exit safely – Option 4 saves all progress to progress.json.

📊 Example
vbnet
Copy code
=== 🧠 Smart Quiz & Study Tracker ===

Menu:
1. Take Quiz
2. View Progress (by ID)
3. View Leaderboard
4. Exit
Enter choice: 1

Enter your Name: Alice
Enter your ID: A01

Available Categories:
1. Python Basics
2. Control Flow
Select category number: 1

Which keyword is used to create a class in Python?
1. class
2. def
3. object
4. module
Your answer: 1
✅ Correct!

🎉 Your Score in Python Basics: 6/7
🛠️ Key Concepts Practiced
File handling (open, with open)

JSON serialization (json.load, json.dump)

Dictionaries & nested structures

Loops (for, while True)

Input validation (isdigit, range checks)

Sorting with lambda

🚀 Future Improvements
Add a reset progress feature.

Allow adding new questions from the app.

Add difficulty levels (easy, medium, hard).

Export leaderboard as CSV/Excel.

👨‍💻 Author
Made with ❤️ using Python as a learning project.