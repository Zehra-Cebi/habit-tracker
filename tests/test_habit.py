from habit import Habit
from datetime import date, timedelta


def test_check_off():
    """
    Tests if today's date is correctly added when checking off a habit.
    """
    habit = Habit("Meditation", "Meditate for 10 minutes", "daily")
    today = date.today()

    habit.check_off()

    assert today in habit.check_ins
    assert len(habit.check_ins) == 1


def test_current_streak_daily():
    """
    Tests if the current streak is correctly calculated for a daily habit.
    """
    habit = Habit("Exercise", "Go running", "daily")
    today = date.today()
    yesterday = today - timedelta(days=1)

    habit.check_ins = [yesterday, today]

    assert habit.current_streak() == 2


def test_current_streak_weekly():
    """
    Tests if the current streak is correctly calculated for a weekly habit.
    """
    habit = Habit("Call parents", "Call once a week", "weekly")
    today = date.today()
    last_week = today - timedelta(days=7)

    habit.check_ins = [last_week, today]

    assert habit.current_streak() == 2


def test_habit_skipped_daily():
    """
    Tests if a daily habit is detected as skipped when last check-in was two days ago.
    """
    habit = Habit("Daily journal", "Write something daily", "daily")
    two_days_ago = date.today() - timedelta(days=2)
    habit.check_ins = [two_days_ago]

    assert habit.habit_skipped() is True


def test_habit_skipped_weekly():
    """
    Tests if a weekly habit is detected as skipped when last check-in was ten days ago.
    """
    habit = Habit("Grocery shopping", "Buy groceries weekly", "weekly")
    ten_days_ago = date.today() - timedelta(days=10)
    habit.check_ins = [ten_days_ago]

    assert habit.habit_skipped() is True
