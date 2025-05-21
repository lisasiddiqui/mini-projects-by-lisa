import datetime

# Define keyword sets
positive_words = ["happy", "excited", "great", "productive", "fun", "joy", "love"]
negative_words = ["sad", "angry", "tired", "frustrated", "anxious", "depressed", "bad"]

def get_sentiment(entry):
    entry = entry.lower()
    score = 0

    for word in positive_words:
        if word in entry:
            score += 1
    for word in negative_words:
        if word in entry:
            score -= 1

    if score > 0:
        return "🙂 Positive"
    elif score < 0:
        return "🙁 Negative"
    else:
        return "😐 Neutral"

def log_entry():
    print("\n--- Daily Mood Journal ---")
    entry = input("How was your day today? Write freely:\n")
    sentiment = get_sentiment(entry)
    today = datetime.date.today().strftime("%Y-%m-%d")

    with open("mood_log.txt", "a") as file:
        file.write(f"{today} | Sentiment: {sentiment} | Entry: {entry}\n")

    print(f"\nEntry saved! Detected Mood: {sentiment}")

def read_past_entries():
    print("\n--- Mood Journal History ---")
    try:
        with open("mood_log.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No entries found yet!")

def main():
    while True:
        print("\nOptions:")
        print("1. Write today's mood entry")
        print("2. View past entries")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            log_entry()
        elif choice == '2':
            read_past_entries()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()
