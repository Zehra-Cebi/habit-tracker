from datetime import date, timedelta
from habit_manager import HabitManager
from habit import Habit


def test_create_and_get_habit():
    """
    Tests creating a habit and retrieving it.
    """
    manager = HabitManager()
    manager.create_habit("Workout", "Do 30 minutes of exercise.", "daily")
    habit = manager.get_habit("Workout")
    assert habit is not None
    assert habit.name == "Workout"
    assert habit.frequency == "daily"


def test_add_existing_habit():
    """
    Tests adding a pre-existing habit to the manager.
    """
    manager = HabitManager()
    habit = Habit("Meditation", "Meditate for 10 minutes.", "daily")
    manager.add_habit(habit)
    assert habit in manager.habits


def test_remove_habit():
    """
    Tests removing a habit by name.
    """
    manager = HabitManager()
    habit = Habit("Journaling", "Write in journal every night.", "daily")
    manager.add_habit(habit)
    manager.remove_habit("Journaling")
    assert manager.get_habit("Journaling") is None


def test_habits_by_frequency():
    """
    Tests filtering habits by their frequency (daily or weekly).
    """
    manager = HabitManager()
    manager.create_habit("Reading", "Read 20 pages.", "daily")
    manager.create_habit("Grocery Shopping", "Weekly grocery trip.", "weekly")
    dailies = manager.habits_by_frequency("daily")
    weeklies = manager.habits_by_frequency("weekly")

    assert len(dailies) == 1
    assert dailies[0].name == "Reading"
    assert len(weeklies) == 1
    assert weeklies[0].name == "Grocery Shopping"


def test_longest_streak_empty():
    """
    Tests that longest streak returns (None, 0) if no habits exist.
    """
    manager = HabitManager()
    habit, streak = manager.longest_streak()
    assert habit is None
    assert streak == 0


def test_longest_daily_streak_empty():
    """
    Tests that longest daily streak returns (None, 0) if no daily habits exist.
    """
    manager = HabitManager()
    habit, streak = manager.longest_daily_streak()
    assert habit is None
    assert streak == 0

def test_longest_streak():
    """
    Tests if the longest_streak method returns the correct habit and streak.
    """
    manager = HabitManager()
    habit1 = Habit("Meditation", "Breathe daily", "daily")
    habit2 = Habit("Run", "Jog daily", "daily")

    today = date.today()
    habit1.check_ins = [today - timedelta(days=2), today - timedelta(days=1), today]
    habit2.check_ins = [today - timedelta(days=1), today]

    manager.add_habit(habit1)
    manager.add_habit(habit2)

    top_habit, streak = manager.longest_streak()
    assert top_habit.name == "Meditation"
    assert streak == 3


def test_longest_daily_streak():
    """
    Tests if the longest_daily_streak method correctly filters by daily frequency.
    """
    manager = HabitManager()
    habit1 = Habit("Weekly walk", "Walk once a week", "weekly")
    habit2 = Habit("Journal", "Write every day", "daily")

    today = date.today()
    habit1.check_ins = [today - timedelta(days=7)]
    habit2.check_ins = [today - timedelta(days=1), today]

    manager.add_habit(habit1)
    manager.add_habit(habit2)

    top_habit, streak = manager.longest_daily_streak()
    assert top_habit.name == "Journal"
    assert streak == 2