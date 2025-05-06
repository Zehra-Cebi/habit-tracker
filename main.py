import questionary
from habit_manager import HabitManager
from db import get_db, save_habit, load_habits
from fixtures import generate_test_habits
from analyze import (
    list_all_habits,
    list_habits_by_frequency,
    get_longest_streak_overall,
    get_longest_streak_of,
    skipped_habits,
    checkin_counts,
    habits_by_streak,
    average_streak,
    habit_frequency_summary)

def main():
    """
    Main loop of the habit tracker CLI app.
    Connects to the SQLite database, loads habits, and shows interactive options.
    """

    try:
        db = get_db()
        if db is None:
            print("Could not connect to the database.")
            return

        print("Welcome to the Habit Tracker App!")
        input("Press Enter to continue...\n")

        manager = HabitManager()
        habits = load_habits(db)
        for habit in habits:
            manager.add_habit(habit)

        demo_loaded = False  # Prevent multiple demo loads

        while True:
            action = questionary.select(
                "Choose an action:",
                choices=[
                    "Create new habit",
                    "Edit existing habit",
                    "Delete habit",
                    "Analyze habit(s)",
                    "Load demo data (4 weeks)",
                    "Exit"
                ]
            ).ask()

            if action == "Create new habit":
                name = questionary.text("Enter a name for the habit:").ask()
                description = questionary.text("Describe the habit:").ask()
                frequency = questionary.select("Choose frequency:", choices=["daily", "weekly"]).ask()

                if name and description and frequency:
                    manager.create_habit(name, description, frequency)
                    print(f"Habit '{name}' has been created.")
                else:
                    print("Invalid input. Please try again.")

            elif action == "Edit existing habit":
                if not manager.habits:
                    print("No habits found.")
                    continue

                name = questionary.select("Choose a habit to edit:", choices=[h.name for h in manager.habits]).ask()
                habit = manager.get_habit(name)

                edit_action = questionary.select(
                    f"What would you like to edit for '{name}'?",
                    choices=[
                        "Check off (mark as done today)",
                        "Rename habit",
                        "Change description",
                        "Change frequency",
                        "Back"
                    ]
                ).ask()

                if edit_action == "Check off (mark as done today)":
                    habit.check_off()
                    print(f"Checked-in recorded for: {habit.name}")

                elif edit_action == "Rename habit":
                    new_name = questionary.text("New name:").ask()
                    if new_name:
                        habit.original_name = habit.name
                        habit.name = new_name
                        print("Habit renamed.")

                elif edit_action == "Change description":
                    new_desc = questionary.text("New description:").ask()
                    if new_desc:
                        habit.description = new_desc
                        print("Description updated.")

                elif edit_action == "Change frequency":
                    new_freq = questionary.select("New frequency:", choices=["daily", "weekly"]).ask()
                    habit.frequency = new_freq
                    print("Frequency updated.")

            elif action == "Delete habit":
                if not manager.habits:
                    print("No habits available to delete.")
                    continue
                name = questionary.select("Select a habit to delete:", choices=[h.name for h in manager.habits]).ask()
                manager.remove_habit(name)
                print(f"Habit '{name}' deleted.")

            elif action == "Analyze habit(s)":
                analyze_action = questionary.select(
                    "Choose an analysis:",
                    choices=[
                        "Basic analysis",
                        "Advanced analysis",
                        "Back"
                    ]
                ).ask()

                if analyze_action == "Basic analysis":
                    basic_choice = questionary.select(
                        "Select basic analysis:",
                        choices=[
                            "List all habits",
                            "List habits by frequency",
                            "Longest streak overall",
                            "Longest streak by name",
                            "Skipped habits",
                            "Back"
                        ]
                    ).ask()

                    if basic_choice == "List all habits":
                        names = list_all_habits(manager.habits)
                        print("\nCurrently  tracked habits:")
                        for name in names:
                            print(f"- {name}")

                    elif basic_choice == "List habits by frequency":
                        freq = questionary.select("Frequency:", choices=["daily", "weekly"]).ask()
                        filtered = list_habits_by_frequency(manager.habits, freq)
                        print(f"\nHabits with '{freq}' frequency:")
                        for habit in filtered:
                            print(f"- {habit.name} (Streak: {habit.current_streak()})")

                    elif basic_choice == "Longest streak overall":
                        habit, streak = get_longest_streak_overall(manager.habits)
                        if habit:
                            print(f"\nLongest streak overall: {habit.name} ({streak})")
                        else:
                            print("No habits available.")

                    elif basic_choice == "Longest streak by name":
                        name = questionary.select("Select habit:", choices=[h.name for h in manager.habits]).ask()
                        streak = get_longest_streak_of(manager.habits, name)
                        print(f"\n'{name}' has a current streak of {streak} days or weeks.")

                    elif basic_choice == "Skipped habits":
                        skipped = skipped_habits(manager.habits)
                        if not skipped:
                            print("No habits were skipped. 🎉")
                        else:
                            print("\nSkipped habits:")
                            for habit in skipped:
                                print(f"- {habit.name}")

                elif analyze_action == "Advanced analysis":
                    advanced_choice = questionary.select(
                        "Select an advanced analysis option:",
                        choices=[
                            "Check-in count per habit",
                            "Habits sorted by streak",
                            "Average streak length",
                            "Summary: daily vs. weekly",
                            "Back"
                        ]
                    ).ask()

                    if advanced_choice == "Check-in count per habit":
                        print("\nCheck-in counts:")
                        for name, count in checkin_counts(manager.habits):
                            print(f"- {name}: {count} check-ins")

                    elif advanced_choice == "Habits sorted by streak":
                        print("\nHabits sorted by current streak:")
                        for habit in habits_by_streak(manager.habits):
                            print(f"- {habit.name}: {habit.current_streak()}")

                    elif advanced_choice == "Average streak length":
                        avg = average_streak(manager.habits)
                        print(f"\nAverage streak: {avg:.2f} check-ins")

                    elif advanced_choice == "Summary: daily vs. weekly":
                        summary = habit_frequency_summary(manager.habits)
                        print("\nHabit frequency summary:")
                        for freq, count in summary.items():
                            print(f"- {freq}: {count} habits")

            elif action == "Load demo data (4 weeks)":
                if demo_loaded:
                    print("Demo data has already been loaded.")
                else:
                    demo_habits = generate_test_habits()
                    for demo in demo_habits:
                        manager.add_habit(demo)
                    demo_loaded = True
                    print("Demo habits loaded (4 weeks of check-ins).")

            elif action == "Exit":
                try:
                    for habit in manager.habits:
                        save_habit(db, habit)
                    print("Habits saved. Goodbye!")
                except Exception as error:
                    print(f"Error saving habits: {error}")
                break

    except KeyboardInterrupt:
        print("\nExited by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
