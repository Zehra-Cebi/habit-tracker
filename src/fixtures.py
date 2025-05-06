from datetime import date
from habit import Habit

def generate_test_habits():
    """
    Creates and returns five predefined habits including their example check-in data for 4 weeks.
    Useful for demonstration, testing, or initial setup.
    """

    habits = []

    def iso_list(dates):
        return [date.fromisoformat(d) for d in dates]

    # Habit 1: Read a book – weekly habit
    h1 = Habit("Read a book", "Read at least 20 pages of a book you're currently reading.", "weekly")
    h1.check_ins = iso_list([
        "2025-01-05",
        "2025-01-12",
        "2025-01-26"
    ])
    habits.append(h1)

    # Habit 2:  Try a new recipe - weekly habit
    h2 = Habit("Try a new recipe", "Try a new recipe to broaden your cooking skills.", "weekly")
    h2.check_ins = iso_list([
        "2025-01-04",
        "2025-01-11",
        "2025-01-18",
        "2025-01-25"
    ])
    habits.append(h2)

    # Habit 3: Stay social – daily habit
    h3 = Habit("Stay social", "Call a family member or good friend every day to stay connected.", "daily")
    h3.check_ins = iso_list([
        "2025-01-01",
        "2025-01-02",
        "2025-01-03",
        "2025-01-04",
        "2025-01-05",

        "2025-01-09",
        "2025-01-10",
        "2025-01-11",
        "2025-01-12",
        "2025-01-13",
        "2025-01-14",
        "2025-01-15",

        "2025-01-18",
        "2025-01-19",
        "2025-01-20",
        "2025-01-21",
        "2025-01-22"
    ])
    habits.append(h3)

    # Habit 4: Listen to Blinkist – daily habit
    h4 = Habit("Listen to Blinkist", "Listen to one book summary (Blink) from Blinkist every day for inspiration", "daily")
    h4.check_ins = iso_list([
        "2025-01-01",
        "2025-01-02",
        "2025-01-03",
        "2025-01-04",
        "2025-01-05",
        "2025-01-06",
        "2025-01-07",
        "2025-01-08",
        "2025-01-09",
        "2025-01-10",
        "2025-01-11",
        "2025-01-12",
        "2025-01-13",
        "2025-01-14",
        "2025-01-15",
        "2025-01-16",
        "2025-01-17",
        "2025-01-18",
        "2025-01-19",
        "2025-01-20",
        "2025-01-21",
        "2025-01-22",
        "2025-01-23",
        "2025-01-24",
        "2025-01-25",
        "2025-01-26",
        "2025-01-27",
        "2025-01-28"
    ])
    habits.append(h4)

    # Habit 5: Yoga practice – daily habit
    h5 = Habit("Yoga practice", "Practice Yoga for 30 minutes daily to improve flexibility and focus.", "daily")
    h5.check_ins = iso_list([
        "2025-01-01",
        "2025-01-02",
        "2025-01-03",
        "2025-01-04",
        "2025-01-05",
        "2025-01-06",
        "2025-01-07",

        "2025-01-12",
        "2025-01-13",
        "2025-01-14",
        "2025-01-15",

        "2025-01-23",
        "2025-01-24",
        "2025-01-25"
    ])
    habits.append(h5)

    return habits
