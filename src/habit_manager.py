from habit import Habit

class HabitManager:
    """
    Manages a collection of habit objects like creation, filtering, analysis, etc.
    """

    def __init__(self):
        """
        Initializes an empty list to store Habit instances.
        """

        self.habits = []

    def add_habit(self, habit):
        """
        Adds an existing Habit object to the list.

        :param habit: An instance of Habit to be added.
        """

        self.habits.append(habit)

    def create_habit(self, name, description, frequency):
        """
        Creates a new Habit object from the user input and adds it to the list.

        :param name: Name of the new habit.
        :param description: Short description of the new habit.
        :param frequency: Frequency ('daily' or 'weekly') of the new habit
        """
        habit = Habit(name, description, frequency)
        self.add_habit(habit)

    def remove_habit(self, name):
        """
        Removes a habit from the list.
        :param name: The name of the habit to be removed.
        """

        self.habits = [habit for habit in self.habits if habit.name != name]

    def get_habit(self, name):
        """
        Finds a habit by its name.
        :param name: The name of the habit to retrieve.
        :return: Habit instance or None if not found.
        """

        for habit in self.habits:
            if habit.name == name:
                return habit
        return None

    def habits_by_frequency(self, frequency):
        """
        Returns a list of habits filtered by their frequency.

        :param frequency: Frequency 'daily' or 'weekly'.
        :return: List of Habit instances (may be empty).
        """

        return [habit for habit in self.habits if habit.frequency == frequency]

    def longest_streak(self):
        """
        Finds the longest streak among all habits.

        :return: Tuple (Habit, streak length) or (None, 0) if no streak was found.
        """

        if not self.habits:
            return None, 0

        max_streak = 0
        top_habit = None

        for habit in self.habits:
            streak = habit.current_streak()
            if streak > max_streak:
                max_streak = streak
                top_habit = habit
        return top_habit, max_streak

    def longest_daily_streak(self):
        """
        Finds the longest daily streak among all daily habits.
        :return: Tuple (Habit, streak) or (None, 0) if no daily habit was found.
        """

        daily_habits = self.habits_by_frequency('daily')
        if not daily_habits:
            return None, 0

        max_streak = 0
        top_habit = None

        for habit in daily_habits:
            streak = habit.current_streak()
            if streak > max_streak:
                max_streak = streak
                top_habit = habit
        return top_habit, max_streak