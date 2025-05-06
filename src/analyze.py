def list_all_habits(habits):
    """
    Returns the names of all currently tracked habits.

    :param habits: list of Habit objects.
    :return: List of habit names (strings).
    """
    return [habit.name for habit in habits]


def list_habits_by_frequency(habits, frequency):
    """
    Filters habits based on their frequency ('daily' or 'weekly').

    :param habits: list of Habit objects
    :param frequency: Frequency  – 'daily' or 'weekly'
    :return: Filtered list of Habit objects based on frequency
    """
    return [habit for habit in habits if habit.frequency == frequency]


def get_longest_streak_overall(habits):
    """
    Finds the habit with the longest streak overall.

    :param habits: list of Habit objects
    :return: Tuple (Habit, streak length) or (None, 0) if empty
    """
    if not habits:
        return None, 0
    top = max(habits, key=lambda h: h.current_streak())
    return top, top.current_streak()


def get_longest_streak_of(habits, name):
    """
    Gets the current streak for a habit by its name.

    :param habits: list of Habit objects
    :param name: Name of the habit
    :return: Streak value (int), or 0 if not found.
    """
    filtered = [h for h in habits if h.name == name]
    if not filtered:
        return 0
    return filtered[0].current_streak()


def checkin_counts(habits):
    """
    Counts how many check-ins have been recorded for each habit.

    :param habits: List of Habit objects
    :return: List of tuples: (habit name, number of check-ins)
    """
    return [(habit.name, len(habit.check_ins)) for habit in habits]


def skipped_habits(habits):
    """
     Lists all habits that were skipped based on their frequency.


    :param habits: List of Habit objects.
    :return: List of skipped Habit objects.
    """
    return [habit for habit in habits if habit.habit_skipped()]


def habit_frequency_summary(habits):
    """
    Gives an overview of how many habits are daily or weekly.

    :param habits: List of Habit objects.
    :return: Dictionary {'daily': int, 'weekly': int}
    """
    summary = {"daily": 0, "weekly": 0}
    for habit in habits:
        freq = habit.frequency.lower()
        if freq in summary:
            summary[freq] += 1
    return summary


def average_streak(habits):
    """
    Calculates the average streak length across all habits.

    :param habits: List of Habit objects.
    :return: Average streak length (float).
    """
    if not habits:
        return 0
    total = sum(h.current_streak() for h in habits)
    return total / len(habits)


def habits_by_streak(habits):
    """
    Sorts habits by their current streak in descending order.

    :param habits: List of Habit objects.
    :return: Sorted list of Habit objects.
    """
    return sorted(habits, key=lambda h: h.current_streak(), reverse=True)
