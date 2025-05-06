import pytest
from freezegun import freeze_time
from analyze import (
    list_all_habits,
    list_habits_by_frequency,
    get_longest_streak_overall,
    get_longest_streak_of,
    skipped_habits,
    checkin_counts,
    habits_by_streak,
    average_streak,
    habit_frequency_summary
)
from fixtures import generate_test_habits

@pytest.fixture
def demo_habits():
    """Returns 5 predefined habits with realistic check-in data."""
    return generate_test_habits()

def test_list_all_habits(demo_habits):
    """Should return names of all tracked habits."""
    names = list_all_habits(demo_habits)
    assert "Read a book" in names
    assert len(names) == 5

@pytest.mark.parametrize("frequency, expected_count", [
    ("daily", 3),
    ("weekly", 2),
])

def test_list_habits_by_frequency(demo_habits, frequency, expected_count):
    """Should return habits filtered by frequency."""
    filtered = list_habits_by_frequency(demo_habits, frequency)
    assert len(filtered) == expected_count
    for habit in filtered:
        assert habit.frequency == frequency

def test_get_longest_streak_overall(demo_habits):
    """Should return the habit with the longest streak."""
    habit, streak = get_longest_streak_overall(demo_habits)
    assert habit.name == "Listen to Blinkist"
    assert streak > 20

@pytest.mark.parametrize("name, expected", [
    ("Yoga practice", 3),
    ("Read a book", 1),
])

def test_get_longest_streak_of(demo_habits, name, expected):
    """Should return correct streak for given habit name."""
    streak = get_longest_streak_of(demo_habits, name)
    assert streak == expected

@freeze_time("2025-02-05")
def test_skipped_habits(demo_habits):
    """Should identify habits that were skipped recently."""
    skipped = skipped_habits(demo_habits)
    names = [habit.name for habit in skipped]
    assert "Read a book" in names
    assert "Yoga practice" in names
    assert len(skipped) >= 2

def test_checkin_counts(demo_habits):
    """Should return number of check-ins per habit."""
    counts = dict(checkin_counts(demo_habits))
    assert counts["Listen to Blinkist"] == 28
    assert counts["Read a book"] == 3

def test_habits_by_streak(demo_habits):
    """Should return habits sorted by current streak."""
    sorted_habits = habits_by_streak(demo_habits)
    assert sorted_habits[0].name == "Listen to Blinkist"
    assert sorted_habits[-1].name == "Read a book"

def test_average_streak(demo_habits):
    """Should calculate average streak length across habits."""
    avg = average_streak(demo_habits)
    assert avg > 5

def test_habit_frequency_summary(demo_habits):
    """Should return correct count of daily vs weekly habits."""
    summary = habit_frequency_summary(demo_habits)
    assert summary["daily"] == 3
    assert summary["weekly"] == 2
