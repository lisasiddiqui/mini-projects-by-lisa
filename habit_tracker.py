import datetime

FILE_NAME = "habits.txt"

def add_habit(habit):
    today = datetime.date.today().isoformat()
    with open(FILE_NAME, "a") as f:
        f.write(f"{habit} | {today}\n")
    print(f"Habit '{habit}' marked as done for {today}.")

def view_progress():
    try:
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()
            habits = {}
            for line in lines:
                name, date = line.strip().split(" | ")
                if name not in habits:
                    habits[name] = 1
                else:
                    habits[name] += 1
            if not habits:
                print("No habits tracked yet.")
            else:
                print("Habit Progress:")
                for habit, count in habits.items():
                    print(f"{habit}: {count} days")
    except FileNotFoundError:
        print("No habit records found yet.")

def main():
    while True:
        print("\nHABIT TRACKER MENU")
        print("1. Mark Habit as Done")
        print("2. View Progress")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            habit = input("Enter habit name: ").capitalize()
            add_habit(habit)
        elif choice == "2":
            view_progress()
        elif choice == "3":
            print("Exiting Habit Tracker.")
            break
        else:
            print("Invalid option. Please choose 1-3.")

if __name__ == "__main__":
    main()
