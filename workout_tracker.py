from datetime import date

def add_workout(workouts):
    try:
        duration = float(input("Duration in minutes: "))
        if duration <= 0:
            print("Duration must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    category = input("Category (Cardio/Strength/Flexibility/Other): ").strip().title()
    if not category:
        category = "Other"

    note = input("Note (optional): ")

    workout = {
        "date": date.today().isoformat(),
        "duration": duration,
        "category": category,
        "note": note
    }
    workouts.append(workout)
    print("Workout added!")

def view_workouts(workouts):
    if not workouts:
        print("No workouts yet.")
        return

    print(f"{'No.':<5} {'Date':<12} {'Category':<15} {'Duration (min)':>15} {'Note'}")
    print("-" * 60)
    for i, w in enumerate(workouts, start=1):
        print(f"{i:<5} {w['date']:<12} {w['category']:<15} {w['duration']:>15.2f} {w['note']}")

def delete_workout(workouts):
    if not workouts:
        print("No workouts yet.")
        return

    view_workouts(workouts)
    try:
        num = int(input("Enter the number of the workout to delete: "))
        if 1 <= num <= len(workouts):
            deleted = workouts.pop(num - 1)
            print(f"Deleted {deleted['category']} workout of {deleted['duration']} minutes.")
        else:
            print("No workout with that number.")
    except ValueError:
        print("Please enter a whole number.")

def show_summary(workouts):
    if not workouts:
        print("No workouts yet.")
        return

    totals = {}
    monthly_total = 0
    all_time_total = 0
    current_month = date.today().isoformat()[:7]

    for w in workouts:
        totals[w["category"]] = totals.get(w["category"], 0) + w["duration"]
        all_time_total += w["duration"]
        if w["date"].startswith(current_month):
            monthly_total += w["duration"]

    print("--- Summary by category ---")
    for cat, total in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        percentage = (total / all_time_total) * 100
        print(f"{cat:<15} {total:>8.2f} min ({percentage:>5.1f}%)")

    print("-" * 30)
    print(f"{'This month':<15} {monthly_total:>8.2f} min")
    print(f"{'All time':<15} {all_time_total:>8.2f} min")

def main():
    workouts = []
    while True:
        print("\n=== Personal Workout Tracker ===")
        print("1. Add workout")
        print("2. View workouts")
        print("3. Delete workout")
        print("4. Summary")
        print("0. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_workout(workouts)
        elif choice == "2":
            view_workouts(workouts)
        elif choice == "3":
            delete_workout(workouts)
        elif choice == "4":
            show_summary(workouts)
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
