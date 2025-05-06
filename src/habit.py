from datetime import date

class Habit:
    """
    A habit that the user wants to build or track over time.
    """

    def __init__(self, name: str, description: str, frequency: str):
        """
        Initializes a new habit with the provided name, description and frequency.

        :param name: Name of the habit.
        :param description: Short description of the habit.
        :param frequency: Frequency ('daily' or 'weekly') of the habit.
        """
        self.name = name
        self.description = description
        self.frequency = frequency  # 'daily' or 'weekly'
        self.created_at = date.today()
        self.check_ins = []

    def check_off(self):
        """
        Marks today's date as as completed for the habit.
        """
        today = date.today()
        if today not in self.check_ins:
            self.check_ins.append(today)

    def current_streak(self):
        """
        Calculates how many times in a row this habit was done.

        :return: Length of current streak in days or weeks.
        """
        if not self.check_ins:
            return 0

        streak = 1
        sorted_check_ins = sorted(self.check_ins, reverse=True)
        current = sorted_check_ins[0]

        for check_in in sorted_check_ins[1:]:
            delta_days = (current - check_in).days
            if self.frequency == 'daily' and delta_days == 1:
                streak += 1
            elif self.frequency == 'weekly' and 0 < delta_days <= 7:
                streak += 1
            else: # streak is broken
                break
            current = check_in
        return streak

    def habit_skipped(self):
        """
        Checks whether the habit has been missed based on its frequency.

        :return: True if the expected check-in interval was missed, else False.
        """
        if not self.check_ins:
            return True

        last_check = max(self.check_ins)
        days_since = (date.today() - last_check).days

        if self.frequency == 'daily':
            return days_since > 1
        elif self.frequency == 'weekly':
            return days_since > 7
        return False

    def __str__(self):
        """
        Simple string representation of the habit for displaying in the CLI.

        :return: String including name, frequency, and current streak.
        """
        return f"{self.name} ({self.frequency}) - Streak: {self.current_streak()}"

