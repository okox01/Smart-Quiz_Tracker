def view_progress(progress, user_id):
    if user_id not in progress:
        print("📭 No progress yet for this user.")
        return
    print(f"\n📊 Progress for {progress[user_id]['name']}:")
    for cat, scores in progress[user_id]["scores"].items():
        avg = sum(scores)/len(scores)
        print(f"- {cat}: Attempts {len(scores)}, Average Score: {avg:.2f}")